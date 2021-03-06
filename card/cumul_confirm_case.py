# -*- coding: utf-8 -*-
import math
import plotly.graph_objs as go
import textwrap

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from translation import _


def get_layout(d):
    # graph config
    xaxis_limit = 40  # days since 100th case
    yaxis_limit = 5.5  # confirm case (logarithmic scale)

    thailand_color = '#0703ff'

    focus_country = [
        'US', 'Spain', 'Italy',
        'China', 'Iran', 'United Kingdom',
        'Japan', 'Singapore', 'Hong Kong',
        'Korea, South', 'Germany',
    ]
    country_palette = [
        '#DD8452', '#55A868', '#C44E52',
        '#8172B3', '#937860', '#DA8BC3',
        '#8C8C8C', '#CCB974', '#64B5CD',
        '#937860', '#c76e4e',
    ]

    # prepare data for graph
    data = []
    shapes = []
    annotations = []
    date_list = d.get('df_global_case_days').columns.values
    country_name_list = d.get('df_global_case_days').index.tolist()
    country_case_list = d.get('df_global_case_days').to_numpy().tolist()
    country_date_list = d.get('df_global_case_date').to_numpy().tolist()

    def const_country_annot_dict(country_name, case_list, color):
        # adding country name to line
        max_case = max(case_list)

        x = case_list.index(max_case) + 0.5
        y = math.log(max_case, 10) + 0.1

        if x >= xaxis_limit:
            x = xaxis_limit - 2
            y = math.log(case_list[x], 10) + 0.1

        annot_dict = {
            'text': country_name,
            'showarrow': False,
            'x': x,
            'y': y,
            'font': {
                'color': color,
            },
        }

        if country_name == _('Thailand'):
            annot_dict['font']['size'] = 14

        return annot_dict

    # adding line to graph
    for idx, country_name in enumerate(country_name_list):
        scatter_dict = {
            'y': country_case_list[idx],
            'x': date_list,
            'text': country_date_list[idx],
            'name': _(country_name),
            'mode': 'lines',
            'line': {
                'width': 0.5,
                'color': 'grey',
            },
            'marker': {
                'size': 0.5,
                'symbol': 'circle',
            },
            'showlegend': False,
            'opacity': 0.75,
            'hovertemplate': _((
                'Days since 100th case: <b>%{x}</b><br>'
                'Confirm case: <b>%{y:,f}</b><br>'
                'Date: <b>%{text}</b>'
            )),
        }

        if country_name == 'Thailand':
            scatter_dict['mode'] = 'lines+markers'
            scatter_dict['line'] = {
                'width': 2,
                'color': thailand_color,
            }
            scatter_dict['marker'] = {
                'symbol': 'circle',
                'size': 3,
            }
            scatter_dict['showlegend'] = True
            scatter_dict['opacity'] = 1
            annotations.append(
                const_country_annot_dict(
                    country_name=_(country_name),
                    case_list=country_case_list[idx],
                    color=thailand_color,
                )
            )
        elif country_name in focus_country:
            focus_idx = focus_country.index(country_name) - 1
            country_color = country_palette[focus_idx]
            scatter_dict['mode'] = 'lines+markers'
            scatter_dict['line'] = {
                'width': 1,
                'color': country_color
            }
            scatter_dict['marker'] = {
                'symbol': 'circle',
                'size': 2,
            }
            scatter_dict['showlegend'] = True
            scatter_dict['opacity'] = 1
            annotations.append(
                const_country_annot_dict(
                    country_name=_(country_name),
                    case_list=country_case_list[idx],
                    color=country_color,
                )
            )

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
                'y': 3.6,
            }
        },
    ]

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
                    'color': '#a1a1a1',
                    'width': 1,
                    'dash': 'dot'
                },
            },
        )
        annot_dict = {
            'text': _('Double case <br> every {} day(s)').format(
                d_case.get('n_days')
            ),
            'showarrow': False,
            'font': {
                'size': 7,
                'color': '#a1a1a1',
            },
        }
        annotations.append(
            {**annot_dict, **d_case.get('annot_dict')}
        )

    # finalize figure
    layout = go.Layout(
        font={
            'family': 'Sarabun',
        },
        yaxis_type='log',
        height=400,
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
            ],
            'title': {
                'text': _('Cumulative number of confirmed cases'),
                'font': {
                    'size': 5,
                },
            },
            'fixedrange': True,
        },
        xaxis={
            'range': [
                0, xaxis_limit
            ],
            'title': {
                'text': _('Number of days since 100th case'),
                'font': {
                    'size': 5,
                },
            },
            'fixedrange': True,
        },
        showlegend=False,
    )

    fig = go.Figure(
        data=data,
        layout=layout,
    )

    graph = dcc.Graph(
        figure=fig,
        config={
            'modeBarButtonsToRemove': [
                'autoScale2d',
                'lasso2d',
                'hoverCompareCartesian',
            ]
        },
    )

    layout = html.Div(
        [
            html.Div([
                dbc.Card(
                    [
                        dbc.CardHeader(_('Cumulative number of confirm cases, by number of days since 100th case')),
                        dbc.CardBody(
                            [
                                graph
                            ]
                        ),
                        dbc.CardFooter(
                            [
                                html.Small([
                                    _('Data source: '),
                                    html.A(
                                        '2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE',
                                        href='https://github.com/CSSEGISandData/COVID-19',
                                        target='blank',
                                    ),
                                ]),
                                html.Br(),
                                html.Small([
                                    _('Graph reference: '),
                                    html.A(
                                        'https://www.ft.com/coronavirus-latest',
                                        href='https://www.ft.com/coronavirus-latest',
                                        target='blank',
                                    ),
                                ]),
                            ],
                            style={
                                'lineHeight': '1',
                            },
                        ),
                    ],
                    style={'marginBottom': '20px'},
                )
            ], className='col'),
        ],
        className='row',
    )

    return layout
