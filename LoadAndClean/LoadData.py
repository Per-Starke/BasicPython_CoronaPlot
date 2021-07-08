import os
import pandas as pd
import sys


def load_data():
    path = sys.path[1]
    path_covid = path + "/data/RKI_COVID19.csv"
    path_counties = path + "/data/RKI_Corona_Landkreise.csv"

    rki_covid19 = pd.read_csv(path_covid, index_col=0)
    rki_covid19['Meldedatum'] = pd.to_datetime(rki_covid19['Meldedatum'])

    rki_counties = pd.read_csv(path_counties, index_col=0)
    rki_counties = rki_counties.rename(columns={'RS': 'IdLandkreis'})

    rki_counties = rki_counties[['IdLandkreis', 'county']]

    data = rki_covid19.merge(rki_counties, how='left')

    data = data.set_index(data['Meldedatum'])
    data = data.sort_index()
    data = data.drop(columns=['Altersgruppe2', 'Meldedatum'])

    return data


print(load_data())
