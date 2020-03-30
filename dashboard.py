# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from card.cumul_confirm_case import get_layout as get_cumul_confirm_case
from card.case_summary import get_layout as get_case_summary

from translation import _
from data_tranform import get_data


d = get_data()

layout = dbc.Container([
    html.H1(
        _('Thailand focus covid-19 dashboard'),
        style={
            'paddingTop': '20px',
            'fontSize': '2rem',
        }
    ),
    html.P(
        _('Data updated: {}').format(d.get('update_date'))
    ),
    get_case_summary(d.get('today_dict')),
    get_cumul_confirm_case(d),
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
        style={'paddingBottom': '20px'},
    ),
])
