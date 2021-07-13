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
