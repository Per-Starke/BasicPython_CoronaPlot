import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from LoadAndClean.Calculate import *


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
    ax.plot(df_inc_total.index, df_inc_total.loc[:, 'CaseCount'], color='green', alpha=0.5,)
    ax.bar(df_inc_total.index, df_inc_total.loc[:, 'DeathcaseCount'], color='green')
    ax.set(xlabel='Day', ylabel='7-Day Incidence')



def plot_incidence_var_age():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variable
    Age.
    """
    # Preparatory Information
    ageGroupLabels = ['Age 0-4', 'Age 5-14', 'Age 15-34', 'Age 35-59', 'Age 60-79', 'Age 80+']
    df_inc_age = calc_incidence_agegroup(df)  # saves all
    agefig = plt.figure()
    ax = agefig.add_subplot(111)
    agefig.suptitle('7-Day Corona Incidence per Age-Group')
    ax.plot(df_inc_age[0].index, df_inc_age[0].loc[:, 'CaseCount'], color='red', alpha=0.5, label=ageGroupLabels[0])
    ax.plot(df_inc_age[1].index, df_inc_age[1].loc[:, 'CaseCount'], color='orange', alpha=0.5, label=ageGroupLabels[1])
    ax.plot(df_inc_age[2].index, df_inc_age[2].loc[:, 'CaseCount'], color='yellow', alpha=0.5, label=ageGroupLabels[2])
    ax.plot(df_inc_age[3].index, df_inc_age[3].loc[:, 'CaseCount'], color='limegreen', alpha=0.5, label=ageGroupLabels[3])
    ax.plot(df_inc_age[4].index, df_inc_age[4].loc[:, 'CaseCount'], color='blue', alpha=0.5, label=ageGroupLabels[4])
    ax.plot(df_inc_age[5].index, df_inc_age[5].loc[:, 'CaseCount'], color='blueviolet', alpha=0.5, label=ageGroupLabels[5])
    ax.bar(df_inc_age[5].index, df_inc_age[5].loc[:, 'DeathcaseCount'], color='blueviolet', alpha=0.5)
    ax.bar(df_inc_age[4].index, df_inc_age[4].loc[:, 'DeathcaseCount'], color='blue', alpha=0.5)
    ax.bar(df_inc_age[3].index, df_inc_age[3].loc[:, 'DeathcaseCount'], color='limegreen', alpha=0.5)
    ax.bar(df_inc_age[2].index, df_inc_age[2].loc[:, 'DeathcaseCount'], color='yellow', alpha=0.5)
    ax.bar(df_inc_age[1].index, df_inc_age[1].loc[:, 'DeathcaseCount'], color='orange', alpha=0.5)
    ax.bar(df_inc_age[0].index, df_inc_age[0].loc[:, 'DeathcaseCount'], color='red', alpha=0.5)

    ax.set(xlabel='Day', ylabel='Line: 7-Day Incidence | Bar: Death Count per 100k')
    ax.legend()


def plot_incidence_var_sex():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variable
    Sex.
    """
    # Preparatory Information
    sexGroupLabels = ['male', 'female', 'unknown gender']
    df_inc_sex = calc_incidence_sex(df)  # saves all
    sexfig = plt.figure()
    ax = sexfig.add_subplot(111)
    sexfig.suptitle('7-Day Corona Incidence per Sex')
    barwidth = 0.3

    # Incidence Line Plots
    ax.plot(df_inc_sex[0].index, df_inc_sex[0].loc[:, 'CaseCount'], color='blue', alpha=0.5, label=sexGroupLabels[0])
    ax.plot(df_inc_sex[1].index, df_inc_sex[1].loc[:, 'CaseCount'], color='red', alpha=0.5, label=sexGroupLabels[1])
    ax.plot(df_inc_sex[2].index, df_inc_sex[2].loc[:, 'CaseCount'], color='green', alpha=0.5, label=sexGroupLabels[2])

    # Death Bar Plots
    ax.bar(df_inc_sex[0].index, df_inc_sex[0].loc[:, 'DeathcaseCount'], color='blue',
           width=-1.5 * barwidth, align='edge')
    ax.bar(df_inc_sex[1].index, df_inc_sex[1].loc[:, 'DeathcaseCount'], color='red',
           width=1.5 * barwidth, align='edge')
    ax.bar(df_inc_sex[2].index, df_inc_sex[2].loc[:, 'DeathcaseCount'], color='green',
           width=barwidth, align='center')

    ax.set(xlabel='Day', ylabel='Line: 7-Day Incidence | Bar: Death Count per 100k')
    ax.legend()


def plot_incidence_var_state():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variable
    State.
    """
    # Preparatory Information
    state_group_labels = states(df)
    df_inc_state = calc_incidence_state(df)  # saves all
    statefig = plt.figure()
    ax = statefig.add_subplot(111)
    statefig.suptitle('7-Day Corona Incidence per State')
    # Incidence Line Plots
    ax.plot(df_inc_state[0].index, df_inc_state[0].loc[:, 'CaseCount'],
           color='black', alpha=0.5, label=state_group_labels[0])
    ax.plot(df_inc_state[1].index, df_inc_state[1].loc[:, 'CaseCount'],
           color='grey', alpha=0.5, label=state_group_labels[1])
    ax.plot(df_inc_state[2].index, df_inc_state[2].loc[:, 'CaseCount'],
           color='red', alpha=0.5, label=state_group_labels[2])
    ax.plot(df_inc_state[3].index, df_inc_state[3].loc[:, 'CaseCount'],
           color='chocolate', alpha=0.5, label=state_group_labels[3])
    ax.plot(df_inc_state[4].index, df_inc_state[4].loc[:, 'CaseCount'],
           color='orange', alpha=0.5, label=state_group_labels[4])
    ax.plot(df_inc_state[5].index, df_inc_state[5].loc[:, 'CaseCount'],
           color='yellow', alpha=0.5, label=state_group_labels[5])
    ax.plot(df_inc_state[6].index, df_inc_state[6].loc[:, 'CaseCount'],
           color='greenyellow', alpha=0.5, label=state_group_labels[6])
    ax.plot(df_inc_state[7].index, df_inc_state[7].loc[:, 'CaseCount'],
           color='lime', alpha=0.5, label=state_group_labels[7])
    ax.plot(df_inc_state[8].index, df_inc_state[8].loc[:, 'CaseCount'],
           color='aquamarine', alpha=0.5, label=state_group_labels[8])
    ax.plot(df_inc_state[9].index, df_inc_state[9].loc[:, 'CaseCount'],
           color='cyan', alpha=0.5, label=state_group_labels[9])
    ax.plot(df_inc_state[10].index, df_inc_state[10].loc[:, 'CaseCount'],
           color='skyblue', alpha=0.5, label=state_group_labels[10])
    ax.plot(df_inc_state[11].index, df_inc_state[11].loc[:, 'CaseCount'],
           color='dodgerblue', alpha=0.5, label=state_group_labels[11])
    ax.plot(df_inc_state[12].index, df_inc_state[12].loc[:, 'CaseCount'],
           color='lightsteelblue', alpha=0.5, label=state_group_labels[12])
    ax.plot(df_inc_state[13].index, df_inc_state[13].loc[:, 'CaseCount'],
           color='navy', alpha=0.5, label=state_group_labels[13])
    ax.plot(df_inc_state[14].index, df_inc_state[14].loc[:, 'CaseCount'],
           color='mediumslateblue', alpha=0.5, label=state_group_labels[14])
    ax.plot(df_inc_state[15].index, df_inc_state[15].loc[:, 'CaseCount'],
           color='blueviolet', alpha=0.5, label=state_group_labels[15])
    # Death Count Bar Plots
    ax.bar(df_inc_state[0].index, df_inc_state[0].loc[:, 'CaseCount'],
            color='black', alpha=0.5)
    ax.bar(df_inc_state[1].index, df_inc_state[1].loc[:, 'CaseCount'],
            color='grey', alpha=0.5)
    ax.bar(df_inc_state[2].index, df_inc_state[2].loc[:, 'CaseCount'],
            color='red', alpha=0.5)
    ax.bar(df_inc_state[3].index, df_inc_state[3].loc[:, 'CaseCount'],
            color='chocolate', alpha=0.5)
    ax.bar(df_inc_state[4].index, df_inc_state[4].loc[:, 'CaseCount'],
            color='orange', alpha=0.5)
    ax.bar(df_inc_state[5].index, df_inc_state[5].loc[:, 'CaseCount'],
            color='yellow', alpha=0.5)
    ax.bar(df_inc_state[6].index, df_inc_state[6].loc[:, 'CaseCount'],
            color='greenyellow', alpha=0.5)
    ax.bar(df_inc_state[7].index, df_inc_state[7].loc[:, 'CaseCount'],
            color='lime', alpha=0.5)
    ax.bar(df_inc_state[8].index, df_inc_state[8].loc[:, 'CaseCount'],
            color='aquamarine', alpha=0.5)
    ax.bar(df_inc_state[9].index, df_inc_state[9].loc[:, 'CaseCount'],
            color='cyan', alpha=0.5)
    ax.bar(df_inc_state[10].index, df_inc_state[10].loc[:, 'CaseCount'],
            color='skyblue', alpha=0.5)
    ax.bar(df_inc_state[11].index, df_inc_state[11].loc[:, 'CaseCount'],
            color='dodgerblue', alpha=0.5)
    ax.bar(df_inc_state[12].index, df_inc_state[12].loc[:, 'CaseCount'],
            color='lightsteelblue', alpha=0.5)
    ax.bar(df_inc_state[13].index, df_inc_state[13].loc[:, 'CaseCount'],
            color='navy', alpha=0.5)
    ax.bar(df_inc_state[14].index, df_inc_state[14].loc[:, 'CaseCount'],
            color='mediumslateblue', alpha=0.5)
    ax.bar(df_inc_state[15].index, df_inc_state[15].loc[:, 'CaseCount'],
            color='blueviolet', alpha=0.5)


    ax.set(xlabel='Day', ylabel='Line: 7-Day Incidence | Bar: Death Count per 100k')
    ax.legend()

#plot_incidence_total()
#plot_incidence_var_age()
# plot_incidence_var_sex()
# plot_incidence_var_state()
# plt.show()
