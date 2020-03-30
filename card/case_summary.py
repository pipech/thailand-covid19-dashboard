import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from translation import _


def get_layout(today_dict):
    def gen_small_info_card(title, class_name=''):
        dif_val = today_dict.get(title).get('dif_val')

        dif_text = _('[Stable]')
        if dif_val > 0:
            dif_text = _('[Increase {:,}]').format(
                today_dict.get(title).get('dif_val')
            )
        elif dif_val < 0:
            dif_text = _('[Decrease {:,}]').format(
                today_dict.get(title).get('dif_val')
            )

        return dbc.Card([
            dbc.CardBody(
                [
                    html.P(
                        _(title),
                        style={
                            'marginBottom': '5px',
                        }
                    ),
                    html.P([
                        html.Span(
                            '{:,}'.format(
                                today_dict.get(title).get('latest_val')
                            ),
                            style={
                                'fontSize': '1.4rem',
                            },
                        ),
                        html.Span(
                            dif_text,
                            style={
                                'fontSize': '0.8rem',
                                'paddingLeft': '10px',
                            },
                        ),
                    ], style={'marginBottom': '0'}),
                ],
                className=class_name,
            ),
        ])

    layout = html.Div(
        [
            html.Div([
                gen_small_info_card(
                    title='Cases',
                    class_name='bg-light',
                ),
            ], className='col-3'),
            html.Div([
                gen_small_info_card(
                    title='Hospitalized',
                ),
            ], className='col-3'),
            html.Div([
                gen_small_info_card(
                    title='Remedied',
                ),
            ], className='col-3'),
            html.Div([
                gen_small_info_card(
                    title='Deceased',
                ),
            ], className='col-3'),
        ],
        className='row',
        style={
            'paddingBottom': '20px',
        },
    )

    return layout
