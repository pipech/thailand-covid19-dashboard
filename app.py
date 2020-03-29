import dash
import dash_bootstrap_components as dbc

from dashboard import layout


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
app.layout = layout

# for aws elasticbeanstalk
application = app.server

if __name__ == '__main__':
    # for development
    app.run_server(
        debug=True,
    )
