# -*- coding: utf-8 -*-
import plotly.graph_objs as go

from data_tranform import df_global_infected_day


# graph config
xaxis_limit = 40  # days since 100th case
yaxis_limit = 5.5  # confirm case (logarithmic scale)
focus_country = [
    'US', 'Spain', 'Italy',
    'China', 'Iran', 'United Kingdom',
    'Japan', 'Singapore', 'Hong Kong',
]

# prepare data for graph
data = []
date_list = df_global_infected_day.columns.values
country_name_list = df_global_infected_day.index.tolist()
country_value_list = df_global_infected_day.to_numpy().tolist()

# adding line to graph
for idx, country_name in enumerate(country_name_list):
    scatter_dict = {
        'y': country_value_list[idx],
        'x': date_list,
        'name': country_name,
        'mode': 'lines',
        'line': {
            'width': 0.5,
            'color': 'grey',
        },
        'marker': {
            'size': 0.5,
            'symbol': 'circle',
        }
    }

    if country_name == 'Thailand':
        scatter_dict['mode'] = 'lines+markers'
        scatter_dict['line'] = {
            'width': 2,
            'color': 'red',
        }
        scatter_dict['marker'] = {
            'symbol': 'circle',
            'size': 3,
        }
    elif country_name in focus_country:
        scatter_dict['mode'] = 'lines+markers'
        scatter_dict['line'] = {
            'width': 1,
        }
        scatter_dict['marker'] = {
            'symbol': 'circle',
            'size': 2,
        }

    data.append(go.Scatter(scatter_dict))


# adding annotation
def double_case_every_n_days(n, days):
    return 100 * (2 ** ((1 / n) * days))


double_case_list = [
    {
        'n_days': 1,
        'annot_dict': {
            'x': 10,
            'y': 5.2,
        }
    },
    {
        'n_days': 2,
        'annot_dict': {
            'x': 20,
            'y': 5.2,
        }
    },
    {
        'n_days': 3,
        'annot_dict': {
            'x': 30,
            'y': 5.2,
        }
    },
    {
        'n_days': 7,
        'annot_dict': {
            'x': 35,
            'y': 3.4,
        }
    },
]

shapes = []
annotations = []

for d_case in double_case_list:
    shapes.append(
        {
            'type': 'line',
            'x0': 0,
            'y0': 100,
            'x1': xaxis_limit,
            'y1': double_case_every_n_days(
                d_case.get('n_days'),
                xaxis_limit
            ),
            'line': {
                'color': 'rgb(255, 0, 0)',
                'width': 2,
                'dash': 'dot'
            },
        },
    )
    annot_dict = {
        'text': 'Double case <br> every {} day(s)'.format(
            d_case.get('n_days')
        ),
        'showarrow': False,
        # 'font': {
        #     'size': 16,
        #     'color': '#c7c7c7',
        # },
    }
    annotations.append(
        {**annot_dict, **d_case.get('annot_dict')}
    )


# finalize figure
layout = go.Layout(
    yaxis_type='log',
    height=500,
    shapes=shapes,
    annotations=annotations,
    margin={
        'l': 0,
        'r': 0,
        'b': 0,
        't': 0,
    },
    yaxis={
        'range': [
            2, yaxis_limit
        ]
    },
    xaxis={
        'range': [
            0, xaxis_limit
        ]
    }
)

fig = go.Figure(
    data=data,
    layout=layout,
)
