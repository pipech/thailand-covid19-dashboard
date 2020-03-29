# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from card.cumul_confirm_case import fig
from data_tranform import update_date

from translation import _


layout = dbc.Container([
    html.H1(
        _('Thailand focus covid-19 dashboard'),
        style={
            'padding-top': '20px',
            'padding-bottom': '20px',
        }
    ),
    dbc.Card(
        [
            dbc.CardHeader(_('Cumulative number of confirm cases, by number of days since 100th case')),
            dbc.CardBody(
                [
                    dcc.Graph(
                        figure=fig,
                        config={
                            'modeBarButtonsToRemove': [
                                'autoScale2d',
                                'lasso2d',
                                'hoverCompareCartesian',
                            ]
                        },
                    ),
                ]
            ),
            dbc.CardFooter(
                [
                    html.Small([
                        _('Data source: '),
                        html.A(
                            'https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases',
                            href='https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases',
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
                    html.Br(),
                    html.Small(_('Data updated: {}').format(update_date)),
                ],
                style={
                    'line-height': '1',
                },
            ),
        ],
        style={'margin-bottom': '20px'},
    ),
    html.Small(
        [
            'Github: ',
            html.A(
                'thailand-covid19-dashboard',
                href='https://github.com/pipech/thailand-covid19-dashboard',
                target='blank',
            ),
            ' | by ',
            html.A(
                'SpaceCode',
                href='https://spacecode.co.th',
                target='blank',
            ),

        ],
        style={'padding-bottom': '20px'},
    ),
])
