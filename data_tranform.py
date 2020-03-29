import pandas as pd

from datetime import datetime

# read dataset
df_thai = pd.read_excel('dataset/covid-19-daily-2.xlsx')
df_global = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

df_global = df_global.drop(columns=['Lat', 'Long', 'Province/State'])
df_global = df_global.groupby('Country/Region').sum()
df_global.columns = pd.to_datetime(df_global.columns)
update_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def convert_to_days_case(df_global, country):
    # get row
    country_row = df_global.loc[country]

    # select day since 100th case
    case_days = country_row[country_row >= 100]

    # store date
    case_date = case_days.copy()
    case_date = case_date.reset_index()
    case_date = case_date.drop(columns=country)
    case_date = case_date.rename(columns={'index': country})
    case_date[country] = case_date[country].dt.strftime('%Y-%m-%d')
    case_date = case_date.T

    # convert to days in first case
    case_days = case_days.reset_index(drop=True).to_frame().T

    return case_days, case_date


case_df_list_days = []
case_df_list_date = []

for country in df_global.index.values:
    case_days, case_date = convert_to_days_case(df_global, country)
    case_df_list_days.append(case_days)
    case_df_list_date.append(case_date)

df_global_case_days = pd.concat(case_df_list_days)
df_global_case_date = pd.concat(case_df_list_date)
