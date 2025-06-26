import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title="Interactive Histogram Viewer", fillable=True)

# Create a sidebar with an input slider
with ui.sidebar():
    ui.input_slider(
        "selected_number_of_bins",     
        "Number of Bins",            
        5,                             
        50,                            
        25                             
    )

@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    count_of_points: int = 437
    np.random.seed(3)  
    random_data_array = 100 + 15 * np.random.randn(count_of_points)

    plt.hist(
        random_data_array,
        bins=input.selected_number_of_bins(),  
        density=True,                          
        color="pink", edgecolor="black"     
    )
    plt.title("Normalized Histogram of Random Data")
    plt.xlabel("Value")
    plt.ylabel("Density")
