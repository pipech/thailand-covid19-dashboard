# -*- coding: utf-8 -*-
import plotly.graph_objs as go

from data_tranform import df_global_infected_day


data = []

date_list = df_global_infected_day.columns.values
country_name_list = df_global_infected_day.index.tolist()
country_value_list = df_global_infected_day.to_numpy().tolist()

focus_country = [
    'US', 'Spain', 'Italy',
    'China', 'Iran', 'United Kingdom',
    'Japan', 'Singapore', 'Hong Kong',
]

for idx, country_name in enumerate(country_name_list):
    if country_name == 'Thailand':
        line = {
            'width': 5,
            'color': 'red',
        }
    elif country_name in focus_country:
        line = {
            'width': 2,
        }
    else:
        line = {
            'width': 0.5,
            'color': 'grey',
        }
    data.append(
        go.Scatter(
            y=country_value_list[idx],
            x=date_list,
            name=country_name,
            line=line,
        )
    )


def double_case_every_n_days(n, days):
    return 100 * (2 ** ((1 / n) * days))


annotations = []
annot_list = [[1, 10], [2, 20], [3, 30], [7, 35]]
for anot in annot_list:
    annotations.append(
        {
            'type': 'line',
            'x0': 0,
            'y0': 100,
            'x1': anot[1],
            'y1': double_case_every_n_days(anot[0], anot[1]),
            'line': {
                'color': 'rgb(255, 0, 0)',
                'width': 2,
                'dash': 'dot'
            },
        },
    )


g_layout = go.Layout(
    yaxis_type='log',
    height=500,
    shapes=annotations,
    margin={
        'l': 0,
        'r': 0,
        'b': 0,
        't': 0,
    },
)

fig = go.Figure(
    data=data,
    layout=g_layout,
)
