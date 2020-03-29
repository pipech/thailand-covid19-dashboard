import dash
import dash_bootstrap_components as dbc

from dashboard import layout
from translation import _


# meta data
title = _('Thailand focus covid-19 dashboard')
description = _('Covid19 tracking dashboard for Thailand, Daily updated')
url = 'https://covid19.space.codes'

app = dash.Dash(
    __name__,
    meta_tags=[
        # Primary meta tags
        {'name': 'title', 'content': title},
        {'name': 'description', 'content': description},
        # Open graph meta tags
        {'property': 'og:type', 'content': 'website'},
        {'property': 'og:url', 'content': url},
        {'property': 'og:title', 'content': title},
        {'property': 'og:description', 'content': description},
    ],
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
app.title = title
app.layout = layout
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-162149795-1"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'UA-162149795-1');
        </script>

        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""


# for aws elasticbeanstalk
application = app.server

if __name__ == '__main__':
    # for development
    app.run_server(
        debug=True,
    )
