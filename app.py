import dash
import dash_bootstrap_components as dbc

from dashboard import layout


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
app.layout = layout

if __name__ == '__main__':
    app.run_server(
        port=80,
    )
