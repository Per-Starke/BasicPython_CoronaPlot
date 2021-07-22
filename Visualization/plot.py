import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from loadAndClean.LoadData import *
from loadAndClean.Calculate import *

# Import the data via the load_data() function
df = load_data()

def plot_incidence_total():
    """
    Generates a bar-plot of the total 7-day incidence values on each day 
    for the date range 02.01.2020 - 07.07.2021
    """
    df_inc_total = calc_incidence_total(df)
    totalfig = plt.figure()
    ax = totalfig.add_subplot(111)
    totalfig.suptitle('7-Day Corona Incidence Total')
    ax.bar(df_inc_total.index, df_inc_total, color='g')
    ax.set(xlabel='Day', ylabel='7-Day Incidence')

def plot_incidence_var_age():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variables
    1. Age Group, 2. Sex, 3. County, 4. Comparison of 1-3
    """
    # Preparatory Information
    agesGroupLabels = ['Age 0-4', 'Age 5-14', 'Age 15-34', 'Age 35-59', 'Age 60-79', 'Age 80+']
    i = 0
    df_inc_age = calc_incidence_agegroup(df)  # saves all
    agefig, axs = plt.subplots(6)
    agefig.suptitle('7-Day Corona Incidence per Age-Group')
    axs[0].bar(df_inc_age[0].index, df_inc_age[0], color = 'g')
    axs[1].bar(df_inc_age[1].index, df_inc_age[1], color = 'r')
    axs[2].bar(df_inc_age[2].index, df_inc_age[2], color = 'b')
    axs[3].bar(df_inc_age[3].index, df_inc_age[3], color = '#26f4c4')
    axs[4].bar(df_inc_age[4].index, df_inc_age[4], color = '#000000')
    axs[5].bar(df_inc_age[5].index, df_inc_age[5], color = 'pink')
    #axs[6].bar(df_inc_age[6].index, df_inc_age[6]) # unknown is empty anyways
    # naming the axes as x: "Day" and y: "7-Day Incidence"
    for ax in axs.flat:
        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()
        ax.set(xlabel='Day', ylabel='7-Day Incidence')
        ax.set_title(agesGroupLabels[i], loc = 'left')
        i += 1

def plot_incidence_var():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variables
    1. Age Group, 2. Sex, 3. County, 4. Comparison of 1-3
    """
    # Preparatory Information
    agesGroupLabels = ['Age 0-4', 'Age 5-14', 'Age 15-34', 'Age 35-59', 'Age 60-79', 'Age 80+']
    width = 0.5
    df_inc_age = calc_incidence_agegroup(df)  # saves all
    x_days = df_inc_age[0].index
    agefig = plt.figure()
    ax = agefig.add_subplot(111)
    agefig.suptitle('7-Day Corona Incidence per Age-Group')
    ax.bar(df_inc_age[0].index, df_inc_age[0], -width,  color = 'g', label = '1', align = 'edge')
    ax.bar(df_inc_age[1].index, df_inc_age[1], width,  color = 'r', label = '2', align = 'edge')
    ax.legend()

    print(df_inc_age)

# stacked bars to put death count into the plots

plot_incidence_total()
plot_incidence_var()

plt.show()