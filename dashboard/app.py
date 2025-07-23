import prices
import pickle
from shiny import reactive, render
from shiny.express import ui





# ------------------------------------------------
# This refreshes the page
# ------------------------------------------------


UPDATE_INTERVAL_SECS: int = 120

@reactive.calc()
def reactive_calc_combined():

    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # call the methods to get the data
    aapl_price=prices.get_aapl_price()



    nvda_price=prices.get_nvda_price()

    # Get a timestamp for "now" and use string format strftime() method to format it
    #timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    latest_dictionary_entry = {"aapl": aapl_price, "nvda": nvda_price}

    # Return everything we need (nothing to return)
    return latest_dictionary_entry




# ------------------------------------------------
# Define the Shiny UI Page layout - Page Options
# ------------------------------------------------


ui.page_opts(title="Stock Price Page Live", fillable=True)

# ------------------------------------------------
# Define the Shiny UI Page layout - Sidebar
# ------------------------------------------------

with ui.sidebar(open="open"):
    ui.h2("Stock prices", class_="text-center")
    ui.p(
        "A demonstration of real-time stock quotes.",
        class_="text-center",
    )


#---------------------------------------------------------------------
# In Shiny Express, everything not in the sidebar is in the main panel
#---------------------------------------------------------------------


ui.h2("Current AAPL")

@render.text
def display_aapl():
    """Get the latest reading"""
    latest_entry = reactive_calc_combined()
    return f"{latest_entry['aapl']}"




ui.hr()

ui.h2("Current NVDA")

@render.text
def display_nvda():
    """Get the latest reading"""
    latest_entry_n = reactive_calc_combined()
    return f"{latest_entry_n['nvda']}"
