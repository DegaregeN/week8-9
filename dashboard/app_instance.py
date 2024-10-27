
# app_instance.py
import dash
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap CSS
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Access the underlying Flask server
server = app.server
