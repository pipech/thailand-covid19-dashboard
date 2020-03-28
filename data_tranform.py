import pandas as pd


# read dataset
df_thai = pd.read_excel('dataset/covid-19-daily-2.xlsx')
df_global = pd.read_csv('dataset/time_series_covid19_confirmed_global.csv')

df_global = df_global.drop(columns=['Lat', 'Long', 'Province/State'])
df_global = df_global.groupby('Country/Region').sum()
df_global.columns = pd.to_datetime(df_global.columns)


def convert_to_days_infected(df_global, country):
    # get row
    country_row = df_global.loc[country]

    # select day since 100th case
    infected_days = country_row[country_row >= 100]

    # convert to days in first infected
    infected_days = infected_days.reset_index(drop=True)

    return infected_days


infected_df_list = []

for country in df_global.index.values:
    infected_df_list.append(
        convert_to_days_infected(df_global, country).to_frame().T
    )

df_global_infected_day = pd.concat(infected_df_list)
