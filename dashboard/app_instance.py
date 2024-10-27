import sys
import os

from dash import Dash
import dash_bootstrap_components as dbc
from layout import create_layout  # Assuming the layout code is in layout.py

# app_instance.py
from dash import Dash

# Create your Dash app instance
app = Dash(__name__)

# Define the layout and callbacks (import or define them here)
app.layout = create_layout(app)  

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

