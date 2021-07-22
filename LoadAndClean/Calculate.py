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


def calc_cases_county(data):
    """
    Calculate the total of all cases and deaths, by county
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: the total number of cases grouped by county
    """

    return data_by_county(data).groupby("County").sum().drop(columns=["Population"])


def compute_incidence(data):
    """
    Helper-function
    Sum over all values submitted in one day, then compute 7-day window
    then shift right by 1, because the values from one day are calculated by the 7 days before!
    :param data: the dataframe to work with
    :return: a dataframe with the incidence values for each day
    """
    german_population = 82020000 #82,02 Million
    hundredk_incidence_constant = 100000 #100k is the constant for incidences
    incidence_factor = german_population/hundredk_incidence_constant

    data = data.resample('1d').sum()
    data = data.rolling(7).sum()
    data = data.shift(1, freq='d')
    data = data['CaseCount'].div(incidence_factor).round(0)
    data = data.dropna()

    return data


def calc_incidence_total(data):
    """
    Calculates the 7-day incidence values, for the whole population, for cases and deaths
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: a dataframe with the incidence values for each day
    """

    data = data.drop(columns=["County", "AgeGroup", "Sex", "Population"])

    data = compute_incidence(data)

    return data


def calc_incidence_sex(data):
    """
    Calculates the 7-day incidence values, grouped by sex, for cases and deaths
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: three dataframes with the incidence values for each day, for Male, Female and Unknown
    """

    data = data.drop(columns=["County", "AgeGroup", "Population"])

    data_male = data[data['Sex'] == "M"]
    data_female = data[data['Sex'] == "W"]
    data_unknown = data[data['Sex'] == "unknown"]

    return compute_incidence(data_male), compute_incidence(data_female), compute_incidence(data_unknown)


def calc_incidence_agegroup(data):
    """
    Calculates the 7-day incidence values, grouped by age group, for cases and deaths
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: 7 dataframes with the incidence values for each day, one for each age group
    0-4, 5-14, 15-34, 35-59, 60-79, 80+ and unkown
    """

    data = data.drop(columns=["County", "Sex", "Population"])

    return_data = [data[data['AgeGroup'] == "A00-A04"], data[data['AgeGroup'] == "A05-A14"],
                   data[data['AgeGroup'] == "A15-A34"], data[data['AgeGroup'] == "A35-A59"],
                   data[data['AgeGroup'] == "A60-A79"], data[data['AgeGroup'] == "A80+"],
                   data[data['AgeGroup'] == "unknown"]]

    for i in range(0, len(return_data)):
        return_data[i] = compute_incidence(return_data[i])

    return tuple(return_data)


def calc_incidence_county(data):
    """
    Calculates the 7-day incidence values, grouped by age group, for cases and deaths
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: dataframes with the incidence values for each day, one for each county
    """

    data = data.drop(columns=["AgeGroup", "Sex", "Population"])

    return_data = []

    county_list = counties(data)

    for county in county_list:
        return_data.append(data[data['County'] == county])

    for i in range(0, len(return_data)):
        return_data[i] = compute_incidence(return_data[i])

    return tuple(return_data)


# df = load_data()
# print(calc_incidence_county(df))