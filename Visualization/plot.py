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
    print(df_inc_total)
    totalfig = plt.figure()
    ax = totalfig.add_subplot(111)
    totalfig.suptitle('7-Day Corona Incidence Total')
    ax.bar(df_inc_total.index, df_inc_total.loc[:, 'CaseCount'], color='g')
    ax.set(xlabel='Day', ylabel='7-Day Incidence')


def plot_incidence_var_age():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variables
    1. Age Group, 2. Sex, 3. County, 4. Comparison of 1-3
    """
    # Preparatory Information
    ageGroupLabels = ['Age 0-4', 'Age 5-14', 'Age 15-34', 'Age 35-59', 'Age 60-79', 'Age 80+']
    df_inc_age = calc_incidence_agegroup(df)  # saves all
    agefig = plt.figure()
    ax = agefig.add_subplot(111)
    agefig.suptitle('7-Day Corona Incidence per Age-Group')
    ax.bar(df_inc_age[0].index, df_inc_age[0].loc[:, 'CaseCount'], color='red', label=ageGroupLabels[0])
    ax.bar(df_inc_age[1].index, df_inc_age[1].loc[:, 'CaseCount'], color='orange', label=ageGroupLabels[1],
           bottom=df_inc_age[0].loc[:, 'CaseCount'])
    ax.bar(df_inc_age[2].index, df_inc_age[2].loc[:, 'CaseCount'], color='yellow', label=ageGroupLabels[2],
           bottom=sum([df_inc_age[0].loc[:, 'CaseCount'],
                       df_inc_age[1].loc[:, 'CaseCount']]))
    ax.bar(df_inc_age[3].index, df_inc_age[3].loc[:, 'CaseCount'], color='limegreen', label=ageGroupLabels[3],
           bottom=sum([df_inc_age[0].loc[:, 'CaseCount'],
                       df_inc_age[1].loc[:, 'CaseCount'],
                       df_inc_age[2].loc[:, 'CaseCount']]))
    ax.bar(df_inc_age[4].index, df_inc_age[4].loc[:, 'CaseCount'], color='blue', label=ageGroupLabels[4],
           bottom=sum([df_inc_age[0].loc[:, 'CaseCount'],
                       df_inc_age[1].loc[:, 'CaseCount'],
                       df_inc_age[2].loc[:, 'CaseCount'],
                       df_inc_age[3].loc[:, 'CaseCount']]))
    ax.bar(df_inc_age[5].index, df_inc_age[5].loc[:, 'CaseCount'], color='blueviolet', label=ageGroupLabels[5],
           bottom=sum([df_inc_age[0].loc[:, 'CaseCount'],
                       df_inc_age[1].loc[:, 'CaseCount'],
                       df_inc_age[2].loc[:, 'CaseCount'],
                       df_inc_age[3].loc[:, 'CaseCount'],
                       df_inc_age[4].loc[:, 'CaseCount']]))
    ax.legend()


def plot_incidence_var_sex():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variables
    1. Age Group, 2. Sex, 3. County, 4. Comparison of 1-3
    """
    # Preparatory Information
    sexGroupLabels = ['male', 'female', 'unknown']
    df_inc_sex = calc_incidence_sex(df)  # saves all
    sexfig = plt.figure()
    ax = sexfig.add_subplot(111)
    sexfig.suptitle('7-Day Corona Incidence per Sex')
    ax.bar(df_inc_sex[0].index, df_inc_sex[0].loc[:, 'CaseCount'], color='blue', label=sexGroupLabels[0])
    ax.bar(df_inc_sex[1].index, df_inc_sex[1].loc[:, 'CaseCount'], color='red', label=sexGroupLabels[1],
           bottom=df_inc_sex[0].loc[:, 'CaseCount'])
    ax.bar(df_inc_sex[2].index, df_inc_sex[2].loc[:, 'CaseCount'], color='orange', label=sexGroupLabels[2],
           bottom=sum([df_inc_sex[0].loc[:, 'CaseCount'],
                       df_inc_sex[1].loc[:, 'CaseCount']]))
    ax.legend()


def plot_incidence_var_state():
    """
    Generates a bar-plot of the 7-day incidence values depending on the variables
    1. Age Group, 2. Sex, 3. County, 4. Comparison of 1-3
    """
    # Preparatory Information
    state_group_labels = states(df)
    df_inc_state = calc_incidence_state(df)  # saves all
    statefig = plt.figure()
    ax = statefig.add_subplot(111)
    statefig.suptitle('7-Day Corona Incidence per State')
    ax.bar(df_inc_state[0].index, df_inc_state[0].loc[:, 'CaseCount'],
           color='black', label=state_group_labels[0])
    ax.bar(df_inc_state[1].index, df_inc_state[1].loc[:, 'CaseCount'],
           color='grey', label=state_group_labels[1],
           bottom=df_inc_state[0].loc[:, 'CaseCount'])
    ax.bar(df_inc_state[2].index, df_inc_state[2].loc[:, 'CaseCount'],
           color='red', label=state_group_labels[2],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[3].index, df_inc_state[3].loc[:, 'CaseCount'],
           color='chocolate', label=state_group_labels[3],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[4].index, df_inc_state[4].loc[:, 'CaseCount'],
           color='orange', label=state_group_labels[4],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[5].index, df_inc_state[5].loc[:, 'CaseCount'],
           color='yellow', label=state_group_labels[5],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[6].index, df_inc_state[6].loc[:, 'CaseCount'],
           color='greenyellow', label=state_group_labels[6],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[7].index, df_inc_state[7].loc[:, 'CaseCount'],
           color='lime', label=state_group_labels[7],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[8].index, df_inc_state[8].loc[:, 'CaseCount'],
           color='aquamarine', label=state_group_labels[8],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount'],
                       df_inc_state[7].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[9].index, df_inc_state[9].loc[:, 'CaseCount'],
           color='cyan', label=state_group_labels[9],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount'],
                       df_inc_state[7].loc[:, 'CaseCount'],
                       df_inc_state[8].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[10].index, df_inc_state[10].loc[:, 'CaseCount'],
           color='skyblue', label=state_group_labels[10],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount'],
                       df_inc_state[7].loc[:, 'CaseCount'],
                       df_inc_state[8].loc[:, 'CaseCount'],
                       df_inc_state[9].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[11].index, df_inc_state[11].loc[:, 'CaseCount'],
           color='dodgerblue', label=state_group_labels[11],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount'],
                       df_inc_state[7].loc[:, 'CaseCount'],
                       df_inc_state[8].loc[:, 'CaseCount'],
                       df_inc_state[9].loc[:, 'CaseCount'],
                       df_inc_state[10].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[12].index, df_inc_state[12].loc[:, 'CaseCount'],
           color='lightsteelblue', label=state_group_labels[12],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount'],
                       df_inc_state[7].loc[:, 'CaseCount'],
                       df_inc_state[8].loc[:, 'CaseCount'],
                       df_inc_state[9].loc[:, 'CaseCount'],
                       df_inc_state[10].loc[:, 'CaseCount'],
                       df_inc_state[11].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[13].index, df_inc_state[13].loc[:, 'CaseCount'],
           color='navy', label=state_group_labels[13],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount'],
                       df_inc_state[7].loc[:, 'CaseCount'],
                       df_inc_state[8].loc[:, 'CaseCount'],
                       df_inc_state[9].loc[:, 'CaseCount'],
                       df_inc_state[10].loc[:, 'CaseCount'],
                       df_inc_state[11].loc[:, 'CaseCount'],
                       df_inc_state[12].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[14].index, df_inc_state[14].loc[:, 'CaseCount'],
           color='mediumslateblue', label=state_group_labels[14],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount'],
                       df_inc_state[7].loc[:, 'CaseCount'],
                       df_inc_state[8].loc[:, 'CaseCount'],
                       df_inc_state[9].loc[:, 'CaseCount'],
                       df_inc_state[10].loc[:, 'CaseCount'],
                       df_inc_state[11].loc[:, 'CaseCount'],
                       df_inc_state[12].loc[:, 'CaseCount'],
                       df_inc_state[13].loc[:, 'CaseCount']])
           )
    ax.bar(df_inc_state[15].index, df_inc_state[15].loc[:, 'CaseCount'],
           color='blueviolet', label=state_group_labels[15],
           bottom=sum([df_inc_state[0].loc[:, 'CaseCount'],
                       df_inc_state[1].loc[:, 'CaseCount'],
                       df_inc_state[2].loc[:, 'CaseCount'],
                       df_inc_state[3].loc[:, 'CaseCount'],
                       df_inc_state[4].loc[:, 'CaseCount'],
                       df_inc_state[5].loc[:, 'CaseCount'],
                       df_inc_state[6].loc[:, 'CaseCount'],
                       df_inc_state[7].loc[:, 'CaseCount'],
                       df_inc_state[8].loc[:, 'CaseCount'],
                       df_inc_state[9].loc[:, 'CaseCount'],
                       df_inc_state[10].loc[:, 'CaseCount'],
                       df_inc_state[11].loc[:, 'CaseCount'],
                       df_inc_state[12].loc[:, 'CaseCount'],
                       df_inc_state[13].loc[:, 'CaseCount'],
                       df_inc_state[14].loc[:, 'CaseCount']])
           )
    ax.legend()

# plot_incidence_total()
# plot_incidence_var_age()
# plot_incidence_var_sex()
# plot_incidence_var_state()
# plt.show()
