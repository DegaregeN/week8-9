from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout(app):
    return dbc.Container([
        # Header
        dbc.Row([
            dbc.Col(
                html.H1("Fraud Detection Dashboard", className="text-primary text-center mb-2"),  # Header in Primary Color
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6("Interactive visualization of fraud and transaction data", 
                        className="text-info text-center mb-4")  # Subheader in Info Color
            )
        ]),

        # Summary Cards with Custom Colors
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Total Transactions", className="card-title text-dark"),  # Title in Dark Color
                        html.H2(id='total-transactions', className="card-text text-success")  # Value in Green
                    ])
                ], className="mb-2 border border-primary")  # Primary Border
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Fraudulent Transactions", className="card-title text-dark"),
                        html.H2(id='fraud-transactions', className="card-text text-danger")  # Value in Red
                    ])
                ], className="mb-2 border border-warning")  # Warning Border
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Fraud Rate (%)", className="card-title text-dark"),
                        html.H2(id='fraud-rate', className="card-text text-warning")  # Value in Yellow
                    ])
                ], className="mb-2 border border-success")  # Green Border
            ], md=4),
        ]),

        # Dropdown Filters for Year and Month
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Select Year", className="text-secondary"),  # Label in Secondary Color
                    dcc.Dropdown(
                        id='year-dropdown',
                        options=[],
                        value=None,
                        clearable=False
                    )
                ])
            ], md=6),
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Select Month", className="text-secondary"),
                    dcc.Dropdown(
                        id='month-dropdown',
                        options=[],
                        value=None,
                        clearable=False
                    )
                ])
            ], md=6),
        ], className="mb-4"),

        # Graphs: Transactions Over Time & Fraud Pie Chart
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='transactions-over-time', 
                          style={'border': '2px solid #0d6efd', 'border-radius': '10px'})  # Blue Border
            ], md=6),
            dbc.Col([
                dcc.Graph(id='fraud-pie-chart', 
                          style={'border': '2px solid #ffc107', 'border-radius': '10px'})  # Yellow Border
            ], md=6),
        ]),

        # Graphs: Transaction Count per User & Amount Histogram
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='transaction-count-per-user', 
                          style={'border': '2px solid #198754', 'border-radius': '10px'})  # Green Border
            ], md=6),
            dbc.Col([
                dcc.Graph(id='amount-distribution', 
                          style={'border': '2px solid #dc3545', 'border-radius': '10px'})  # Red Border
            ], md=6),
        ]),
    ], fluid=True)
