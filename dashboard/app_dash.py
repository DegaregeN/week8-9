import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Load data
df = pd.read_csv('../data/processed_data.csv')

app.layout = html.Div([
    html.H1('Fraud Detection Dashboard'),
    html.Div([
        html.H2('Summary Statistics'),
        html.P(f'Total Transactions: {df.shape[0]}'),
        html.P(f'Total Fraud Cases: {df[df["Class"] == 1].shape[0]}'),
        html.P(f'Fraud Percentage: {df[df["Class"] == 1].shape[0] / df.shape[0] * 100:.2f}%')
    ]),
    dcc.Graph(
        id='fraud-trend-chart',
        figure=px.line(df, x='Time', y='Class', title='Fraud Cases Over Time')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)