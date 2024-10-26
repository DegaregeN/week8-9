from dash import html, dcc

def serve_layout():
    return html.Div([
        html.H1('Fraud Detection Dashboard'),
        dcc.Graph(id='fraud-cases-over-time'),
        dcc.Graph(id='fraud-by-device')
    ])