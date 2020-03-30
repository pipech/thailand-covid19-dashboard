import pandas as pd

from datetime import datetime


def get_data():
    # read dataset
    df_case = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    df_death = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    df_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    def convert_columns(df):
        df = df.drop(columns=['Lat', 'Long', 'Province/State'])
        df = df.groupby('Country/Region').sum()
        df.columns = pd.to_datetime(df.columns)
        return df

    df_case = convert_columns(df_case)
    df_death = convert_columns(df_death)
    df_recovered = convert_columns(df_recovered)

    today_dict = get_today_dict(df_case, df_death, df_recovered)

    def convert_to_days_case(df_case, country):
        # get row
        country_row = df_case.loc[country]

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

    for country in df_case.index.values:
        case_days, case_date = convert_to_days_case(df_case, country)
        case_df_list_days.append(case_days)
        case_df_list_date.append(case_date)

    data_dict = {
        'df_global_case_days': pd.concat(case_df_list_days),
        'df_global_case_date': pd.concat(case_df_list_date),
        'update_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'today_dict': today_dict,
    }

    return data_dict


def get_today_dict(df_case, df_death, df_recovered):
    # get date
    latest_date = max(df_case.columns)
    last_date = latest_date - pd.DateOffset(1)

    today_dict = {}

    key_df_dict = {
        'Cases': df_case,
        'Deceased': df_death,
        'Remedied': df_recovered,
    }

    # get latest and last value from dataframe
    for key, df in key_df_dict.items():
        latest_val = df.loc['Thailand', latest_date]
        last_val = df.loc['Thailand', last_date]
        today_dict[key] = {
            'latest_val': latest_val,
            'last_val': last_val,
            'dif_val': (latest_val - last_val)
        }

    # get hospitalized value
    today_dict['Hospitalized'] = {}
    val_list = ['latest_val', 'last_val', 'dif_val']
    for val in val_list:
        today_dict['Hospitalized'][val] = (
            today_dict['Cases'][val] -
            today_dict['Deceased'][val] -
            today_dict['Remedied'][val]
        )

    return today_dict
