from copy import deepcopy

from loadAndClean.LoadData import *


def calc_cases_sex(data):
    """
    Calculate the total of all cases and deaths, by sex
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: the total number of cases gouped by sex
    """

    return data_by_sex(data).groupby("Sex").sum()


def calc_cases_agegroup(data):
    """
    Calculate the total of all cases and deaths, by age group
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: the total number of cases grouped by age group
    """

    return data_by_agegroup(data).groupby("AgeGroup").sum()


def calc_cases_states(data):
    """
    Calculate the total of all cases and deaths, by state
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: the total number of cases grouped by state
    """

    return data_by_state(data).groupby("State").sum().drop(columns=["Population"])


def standardize_df_length(data, return_data):
    """
    Helper-function to standardize the length of all dataframes in return_data.
    Reindexes the dataframes so that all dates occur exactly once.
    :param data: the dataframe returned by load_data (probably with some dropped columns)
    :param return_data: the data that should be standardized in it's length - a list of dataframes
    :return: the standardized data as a list of dataframes
    """

    # Fill missing dates, so that all dataframes have the same length:
    all_dates = pd.date_range(start=data.index.min(), end=data.index.max())
    for i in range(len(return_data)):
        return_data[i] = return_data[i].reindex(all_dates).fillna(0)

    return return_data


def compute_incidence(data, incidence_factor):
    """
    Helper-function
    Sum over all values submitted in one day, then compute 7-day window
    then shift right by 1, because the values from one day are calculated by the 7 days before!
    :param incidence_factor: which incidence factor to divide through
    :param data: the dataframe to work with
    :return: a dataframe with the 7 day window values for each day
    """

    data = data.resample('1d').sum()
    data = data.cumsum()
    data = data.shift(1, freq='d')
    data = data.div(incidence_factor).round(0)

    return_data = deepcopy(data)

    # Subtract the values of the 7-day-window before this one, for each day respectively
    for i in range(len(data)):
        if i == 0:
            return_data.iloc[i]["CaseCount"] = 0
            return_data.iloc[i]["DeathcaseCount"] = 0
        else:
            return_data.iloc[i]["CaseCount"] = data.iloc[i]["CaseCount"] - data.iloc[i-1]["CaseCount"]
            return_data.iloc[i]["DeathcaseCount"] = data.iloc[i]["DeathcaseCount"] - data.iloc[i - 1]["DeathcaseCount"]

    return return_data


def calc_incidence_total(data):
    """
    Calculates the 7-day incidence values, for the whole population, for cases and deaths
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: a dataframe with the incidence values for each day
    """

    # german population is a standard constant
    # We could also calculate it, but the standard-constant way is how it is done by RKI as well
    population = 83020000
    incidence_factor = population / 100000

    data = data.drop(columns=["State", "AgeGroup", "Sex", "Population"])

    data = compute_incidence(data, incidence_factor)

    return data


def calc_incidence_sex(data):
    """
    Calculates the 7-day incidence values, grouped by sex, for cases and deaths
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: three dataframes with the incidence values for each day, for Male, Female and Unknown
    """

    data = data.drop(columns=["State", "AgeGroup", "Population"])

    data_male = data[data['Sex'] == "M"]
    data_female = data[data['Sex'] == "W"]
    data_unknown = data[data['Sex'] == "unknown"]

    # We can not get the amount of males/females/unknowns from the given data, so we use standard constants here!
    return_data = [compute_incidence(data_male, 41040000/100000),
                   compute_incidence(data_female, 42000000/100000),
                   compute_incidence(data_unknown, len(data_unknown)*25/100000)]

    return_data = standardize_df_length(data, return_data)

    return tuple(return_data)


def calc_incidence_agegroup(data):
    """
    Calculates the 7-day incidence values, grouped by age group, for cases and deaths
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: 7 dataframes with the incidence values for each day, one for each age group
    0-4, 5-14, 15-34, 35-59, 60-79, 80+ and unknown
    """

    data = data.drop(columns=["State", "Sex", "Population"])

    return_data = [data[data['AgeGroup'] == "A00-A04"], data[data['AgeGroup'] == "A05-A14"],
                   data[data['AgeGroup'] == "A15-A34"], data[data['AgeGroup'] == "A35-A59"],
                   data[data['AgeGroup'] == "A60-A79"], data[data['AgeGroup'] == "A80+"],
                   data[data['AgeGroup'] == "unknown"]]

    # We can not get the amount of people per agegroup from the given data, so we use standard constants here!
    for i in range(len(return_data)):
        if i == 0:
            return_data[i] = compute_incidence(return_data[i], 3157537/100000)
        elif i == 1:
            return_data[i] = compute_incidence(return_data[i], 6760000 / 100000)
        elif i == 2:
            return_data[i] = compute_incidence(return_data[i], 18200000 / 100000)
        elif i == 3:
            return_data[i] = compute_incidence(return_data[i], 27340000 / 100000)
        elif i == 4:
            return_data[i] = compute_incidence(return_data[i], 8000000 / 100000)
        elif i == 5:
            return_data[i] = compute_incidence(return_data[i], 5915000 / 100000)
        elif i == 6:
            return_data[i] = compute_incidence(return_data[i], 10000000 / 100000)

    return_data = standardize_df_length(data, return_data)

    return tuple(return_data)


def calc_incidence_state(data):
    """
    Calculates the 7-day incidence values, grouped by state, for cases and deaths
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: dataframes with the incidence values for each day, one for each state
    """

    state_population_list = state_population(data)

    data = data.drop(columns=["AgeGroup", "Sex", "Population"])

    return_data = []

    state_list = states(data)

    # Add all counties to the return_data
    for state in state_list:
        return_data.append(data[data['State'] == state])

    # For each county, get the population and then compute incidence
    for i in range(0, len(return_data)):
        state = state_list[i]
        pop = state_population_list.loc[state]["Population"]
        return_data[i] = compute_incidence(return_data[i], pop/100000)

    return_data = standardize_df_length(data, return_data)

    return tuple(return_data)
