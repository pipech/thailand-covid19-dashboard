# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from card.cumul_confirm_case import fig

layout = dbc.Container([
    html.H1('Thailand focus covid-19 dashboard'),
    dbc.Card([
        dbc.CardHeader('Cumulative number of confirm cases, by number of days since 100th case'),
        dbc.CardBody(
            [
                dcc.Graph(
                    figure=fig,
                ),
            ]
        ),
        dbc.CardFooter('This is the footer'),
    ]),
])
