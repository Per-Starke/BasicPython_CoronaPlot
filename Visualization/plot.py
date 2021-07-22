import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from loadAndClean.LoadData import *
from loadAndClean.Calculate import *

# Import the data via the load_data() function
df = load_data()

def plot_incidence_time():
    """
    Generates a bar-plot of the total 7-day incidence values on each day 
    for the date range 02.01.2020 - 07.07.2021
    """
    df_incidence_total = calc_incidence_total(df)

    print(df_incidence_total)
    inc_time_plot = df_incidence_total.plot.bar()
    n = 14  # Keeps every Nth label to not overcrowd the x axis
    [l.set_visible(False) for (i, l) in enumerate(inc_time_plot.axes.xaxis.get_ticklabels()) if i % n != 0]


def plot_incidence_var():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variables
    1. Age Group, 2. Sex, 3. County, 4. Comparison of 1-3
    """
    df_incidence_agegroup = calc_incidence_agegroup(df)
    print(df_incidence_agegroup)
    df_incidence_sex = calc_incidence_sex(df)
    print(df_incidence_sex)


# stacked bars to put death count into the plots

#plot_incidence_time()
plot_incidence_var()

plt.show()

