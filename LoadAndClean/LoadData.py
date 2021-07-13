import pandas as pd
import sys
import warnings

"""
Supressing the following warning, as it is not relevant for us:
'FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will 
perform elementwise comparison mask |= (ar1 == a)'
"""
warnings.simplefilter(action='ignore', category=FutureWarning)


def load_data():
    """
    Loads the relevant data from the .csv files
    :return: the data as a pandas dataframe, containing:
    County, AgeGroup, Sex, CaseCount, DeathcaseCount and Population
    """

    # Store the path to the data files
    path = sys.path[1]
    path_covid = path + "/data/RKI_COVID19.csv"
    path_counties = path + "/data/RKI_Corona_Landkreise.csv"

    # Read the corona data
    rki_covid19 = pd.read_csv(path_covid, index_col=0)

    # Use pandas datetime object for the "Meldedatum"
    rki_covid19['Meldedatum'] = pd.to_datetime(rki_covid19['Meldedatum'])

    # Read the counties data
    rki_counties = pd.read_csv(path_counties, index_col=0)
    rki_counties.rename(columns={'RS': 'IdLandkreis'}, inplace=True)

    # We only need the ID and EWZ (number of inhabitants)
    rki_counties = rki_counties[['IdLandkreis', 'EWZ']]

    # left-join the corona data and the counties (Will be joined on the IdLandkreis column)
    data = rki_covid19.merge(rki_counties, how='left')

    # Use the Meldedatum as index and sort by this
    data = data.set_index(data['Meldedatum'])
    data = data.sort_index()

    # Drop all columns that are not interesting for us
    data = data.drop(columns=['IdBundesland', 'Bundesland', 'Datenstand', 'NeuerFall', 'NeuerTodesfall',
                              'Refdatum', 'AnzahlGenesen', 'IstErkrankungsbeginn',
                              'IdLandkreis', 'NeuGenesen', 'Altersgruppe2', 'Meldedatum'])

    # Rename columns to english
    data.rename(columns={"Landkreis": "County", "Altersgruppe": "AgeGroup", "Geschlecht": "Sex",
                         "AnzahlFall": "CaseCount", "AnzahlTodesfall": "DeathcaseCount", "EWZ": "Population"},
                inplace=True)

    # Rename "unbekannt" to "unknown"
    data = data.replace("unbekannt", "unknown")

    return data


def data_by_sex(data):
    """
    Get the relevant columns to further inspect the covid numbers in relation to the sexes
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: Sex, CaseCount and DeathcaseCount from data
    """

    return data[["Sex", "CaseCount", "DeathcaseCount"]]


def data_by_agegroup(data):
    """
    Get the relevant columns to further inspect the covid numbers in relation to the age groups
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: AgeGroup, CaseCount and DeathcaseCount from data
    """

    return data[["AgeGroup", "CaseCount", "DeathcaseCount"]]


def data_by_county(data):
    """
    Get the relevant columns to further inspect the covid numbers in relation to the counties
    :param data: the dataframe to work on - should be the one returned by load_data
    :return: County, CaseCount, DeathcaseCount and Population from data
    """

    return data[["County", "CaseCount", "DeathcaseCount", "Population"]]
