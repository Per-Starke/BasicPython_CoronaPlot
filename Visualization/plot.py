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
    totalfig.suptitle('7-Day Corona Incidence & Deaths  Total')
    ax.plot(df_inc_total.index, df_inc_total.loc[:, 'CaseCount'], color='green', alpha=0.5, label='Germany')
    ax.plot(df_inc_total.index, df_inc_total.loc[:, 'DeathcaseCount'], color='green',
            linestyle='--', label='Deaths Germany')
    ax.set(xlabel='Day', ylabel='Line: 7-Day Incidence | Dashed: Death Count per 100k')
    ax.legend()


def plot_incidence_var_age():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variable
    Age.
    """
    ageGroupLabels = ['Age 0-4', 'Age 5-14', 'Age 15-34', 'Age 35-59', 'Age 60-79', 'Age 80+']
    df_inc_age = calc_incidence_agegroup(df)  # saves all
    agefig = plt.figure()
    ax = agefig.add_subplot(111)
    agefig.suptitle('7-Day Corona Incidence & Deaths per Age-Group')

    ax.plot(df_inc_age[0].index, df_inc_age[0].loc[:, 'CaseCount'], color='red',
            alpha=0.5, label=ageGroupLabels[0])
    ax.plot(df_inc_age[1].index, df_inc_age[1].loc[:, 'CaseCount'], color='orange',
            alpha=0.5, label=ageGroupLabels[1])
    ax.plot(df_inc_age[2].index, df_inc_age[2].loc[:, 'CaseCount'], color='yellow',
            alpha=0.5, label=ageGroupLabels[2])
    ax.plot(df_inc_age[3].index, df_inc_age[3].loc[:, 'CaseCount'], color='limegreen',
            alpha=0.5, label=ageGroupLabels[3])
    ax.plot(df_inc_age[4].index, df_inc_age[4].loc[:, 'CaseCount'], color='blue',
            alpha=0.5, label=ageGroupLabels[4])
    ax.plot(df_inc_age[5].index, df_inc_age[5].loc[:, 'CaseCount'], color='blueviolet',
            alpha=0.5, label=ageGroupLabels[5])
    # Death Dashed Line Plots
    ax.plot(df_inc_age[0].index, df_inc_age[0].loc[:, 'DeathcaseCount'], color='red',
            linestyle='--', label='Deaths ' + ageGroupLabels[0])
    ax.plot(df_inc_age[1].index, df_inc_age[1].loc[:, 'DeathcaseCount'], color='orange',
            linestyle='--', label='Deaths ' + ageGroupLabels[1])
    ax.plot(df_inc_age[2].index, df_inc_age[2].loc[:, 'DeathcaseCount'], color='yellow',
            linestyle='--', label='Deaths ' + ageGroupLabels[2])
    ax.plot(df_inc_age[3].index, df_inc_age[3].loc[:, 'DeathcaseCount'], color='limegreen',
            linestyle='--', label='Deaths ' + ageGroupLabels[3])
    ax.plot(df_inc_age[4].index, df_inc_age[4].loc[:, 'DeathcaseCount'], color='blue',
            linestyle='--', label='Deaths ' + ageGroupLabels[4])
    ax.plot(df_inc_age[5].index, df_inc_age[5].loc[:, 'DeathcaseCount'], color='blueviolet',
            linestyle='--', label='Deaths ' + ageGroupLabels[5])






    ax.set(xlabel='Day', ylabel='Line: 7-Day Incidence | Dashed: Death Count per 100k')
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
    sexfig.suptitle('7-Day Corona Incidence & Deaths per Sex')
    barwidth = 0.3

    # Incidence Line Plots
    ax.plot(df_inc_sex[0].index, df_inc_sex[0].loc[:, 'CaseCount'], color='blue',
            alpha=0.5, label=sexGroupLabels[0])
    ax.plot(df_inc_sex[1].index, df_inc_sex[1].loc[:, 'CaseCount'], color='red',
            alpha=0.5, label=sexGroupLabels[1])
    ax.plot(df_inc_sex[2].index, df_inc_sex[2].loc[:, 'CaseCount'], color='green',
            alpha=0.5, label=sexGroupLabels[2])
    # Death Dashed Line Plots
    ax.plot(df_inc_sex[0].index, df_inc_sex[0].loc[:, 'DeathcaseCount'], color='blue',
           linestyle='--', label='Deaths ' + sexGroupLabels[0])
    ax.plot(df_inc_sex[1].index, df_inc_sex[1].loc[:, 'DeathcaseCount'], color='red',
           linestyle='--', label='Deaths ' + sexGroupLabels[1])
    ax.plot(df_inc_sex[2].index, df_inc_sex[2].loc[:, 'DeathcaseCount'], color='green',
           linestyle='--', label='Deaths ' + sexGroupLabels[2])

    ax.set(xlabel='Day', ylabel='Line: 7-Day Incidence | Dashed: Death Count per 100k')
    ax.legend()


def plot_incidence_var_state():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variable
    State.
    """
    # Preparatory Information
    stateGroupLabels = states(df)
    df_inc_state = calc_incidence_state(df)  # saves all
    statefig = plt.figure()
    ax = statefig.add_subplot(111)
    statefig.suptitle('7-Day Corona Incidence & Deaths per State')
    # Incidence Line Plots
    ax.plot(df_inc_state[0].index, df_inc_state[0].loc[:, 'CaseCount'],
           color='black', alpha=0.5, label=stateGroupLabels[0])
    ax.plot(df_inc_state[1].index, df_inc_state[1].loc[:, 'CaseCount'],
           color='grey', alpha=0.5, label=stateGroupLabels[1])
    ax.plot(df_inc_state[2].index, df_inc_state[2].loc[:, 'CaseCount'],
           color='red', alpha=0.5, label=stateGroupLabels[2])
    ax.plot(df_inc_state[3].index, df_inc_state[3].loc[:, 'CaseCount'],
           color='chocolate', alpha=0.5, label=stateGroupLabels[3])
    ax.plot(df_inc_state[4].index, df_inc_state[4].loc[:, 'CaseCount'],
           color='orange', alpha=0.5, label=stateGroupLabels[4])
    ax.plot(df_inc_state[5].index, df_inc_state[5].loc[:, 'CaseCount'],
           color='yellow', alpha=0.5, label=stateGroupLabels[5])
    ax.plot(df_inc_state[6].index, df_inc_state[6].loc[:, 'CaseCount'],
           color='greenyellow', alpha=0.5, label=stateGroupLabels[6])
    ax.plot(df_inc_state[7].index, df_inc_state[7].loc[:, 'CaseCount'],
           color='lime', alpha=0.5, label=stateGroupLabels[7])
    ax.plot(df_inc_state[8].index, df_inc_state[8].loc[:, 'CaseCount'],
           color='aquamarine', alpha=0.5, label=stateGroupLabels[8])
    ax.plot(df_inc_state[9].index, df_inc_state[9].loc[:, 'CaseCount'],
           color='cyan', alpha=0.5, label=stateGroupLabels[9])
    ax.plot(df_inc_state[10].index, df_inc_state[10].loc[:, 'CaseCount'],
           color='skyblue', alpha=0.5, label=stateGroupLabels[10])
    ax.plot(df_inc_state[11].index, df_inc_state[11].loc[:, 'CaseCount'],
           color='dodgerblue', alpha=0.5, label=stateGroupLabels[11])
    ax.plot(df_inc_state[12].index, df_inc_state[12].loc[:, 'CaseCount'],
           color='lightsteelblue', alpha=0.5, label=stateGroupLabels[12])
    ax.plot(df_inc_state[13].index, df_inc_state[13].loc[:, 'CaseCount'],
           color='navy', alpha=0.5, label=stateGroupLabels[13])
    ax.plot(df_inc_state[14].index, df_inc_state[14].loc[:, 'CaseCount'],
           color='mediumslateblue', alpha=0.5, label=stateGroupLabels[14])
    ax.plot(df_inc_state[15].index, df_inc_state[15].loc[:, 'CaseCount'],
           color='blueviolet', alpha=0.5, label=stateGroupLabels[15])
    # Death Dashed Line Plots
    ax.plot(df_inc_state[0].index, df_inc_state[0].loc[:, 'DeathcaseCount'],
            color='black', linestyle='--', label='Deaths ' + stateGroupLabels[0])
    ax.plot(df_inc_state[1].index, df_inc_state[1].loc[:, 'DeathcaseCount'],
            color='grey', linestyle='--', label='Deaths ' + stateGroupLabels[1])
    ax.plot(df_inc_state[2].index, df_inc_state[2].loc[:, 'DeathcaseCount'],
            color='red', linestyle='--', label='Deaths ' + stateGroupLabels[2])
    ax.plot(df_inc_state[3].index, df_inc_state[3].loc[:, 'DeathcaseCount'],
            color='chocolate', linestyle='--', label='Deaths ' + stateGroupLabels[3])
    ax.plot(df_inc_state[4].index, df_inc_state[4].loc[:, 'DeathcaseCount'],
            color='orange', linestyle='--', label='Deaths ' + stateGroupLabels[4])
    ax.plot(df_inc_state[5].index, df_inc_state[5].loc[:, 'DeathcaseCount'],
            color='yellow', linestyle='--', label='Deaths ' + stateGroupLabels[5])
    ax.plot(df_inc_state[6].index, df_inc_state[6].loc[:, 'DeathcaseCount'],
            color='greenyellow', linestyle='--', label='Deaths ' + stateGroupLabels[6])
    ax.plot(df_inc_state[7].index, df_inc_state[7].loc[:, 'DeathcaseCount'],
            color='lime', linestyle='--', label='Deaths ' + stateGroupLabels[7])
    ax.plot(df_inc_state[8].index, df_inc_state[8].loc[:, 'DeathcaseCount'],
            color='aquamarine', linestyle='--', label='Deaths ' + stateGroupLabels[8])
    ax.plot(df_inc_state[9].index, df_inc_state[9].loc[:, 'DeathcaseCount'],
            color='cyan', linestyle='--', label='Deaths ' + stateGroupLabels[9])
    ax.plot(df_inc_state[10].index, df_inc_state[10].loc[:, 'DeathcaseCount'],
            color='skyblue', linestyle='--', label='Deaths ' + stateGroupLabels[10])
    ax.plot(df_inc_state[11].index, df_inc_state[11].loc[:, 'DeathcaseCount'],
            color='dodgerblue', linestyle='--', label='Deaths ' + stateGroupLabels[11])
    ax.plot(df_inc_state[12].index, df_inc_state[12].loc[:, 'DeathcaseCount'],
            color='lightsteelblue', linestyle='--', label='DeathcaseCount' + stateGroupLabels[12])
    ax.plot(df_inc_state[13].index, df_inc_state[13].loc[:, 'DeathcaseCount'],
            color='navy', linestyle='--', label='Deaths ' + stateGroupLabels[13])
    ax.plot(df_inc_state[14].index, df_inc_state[14].loc[:, 'DeathcaseCount'],
            color='mediumslateblue', linestyle='--', label='Deaths ' + stateGroupLabels[14])
    ax.plot(df_inc_state[15].index, df_inc_state[15].loc[:, 'DeathcaseCount'],
            color='blueviolet', linestyle='--', label='Deaths ' + stateGroupLabels[15])


    ax.set(xlabel='Day', ylabel='Line: 7-Day Incidence | Dashed: Death Count per 100k')
    ax.legend()

plot_incidence_total()
plot_incidence_var_age()
plot_incidence_var_sex()
plot_incidence_var_state()
plt.show()
