import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
from app_instance import app  # Import your app instance

# Load the dataset (update path as needed)
df = pd.read_csv('C:/Users/1221/Desktop/Acadamy AIM 2/week8-9/data/cleaned_fraud_data.csv')

# Convert 'signup_time' and 'purchase_time' into datetime
df['signup_time'] = pd.to_datetime(df['signup_time'])
df['purchase_time'] = pd.to_datetime(df['purchase_time'])

# Ensure 'age' is in a proper numeric format if needed
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Populate dropdown options for Year and Month selection
@app.callback(
    [
        Output('year-dropdown', 'options'),
        Output('year-dropdown', 'value'),
        Output('month-dropdown', 'options'),
        Output('month-dropdown', 'value'),
    ],
    [Input('year-dropdown', 'options')]  # Trigger on load
)
def set_dropdown_options(_):
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])  # Ensure datetime conversion
    years = sorted(df['purchase_time'].dt.year.unique())
    months = sorted(df['purchase_time'].dt.strftime('%B').unique(),
                    key=lambda x: pd.to_datetime(x, format='%B').month)
    year_options = [{'label': year, 'value': year} for year in years]
    month_options = [{'label': month, 'value': month} for month in months]
    return year_options, years[0], month_options, months[0]

# Update summary statistics: Total Transactions, Fraudulent Transactions, and Fraud Rate
@app.callback(
    [
        Output('total-transactions', 'children'),
        Output('fraud-transactions', 'children'),
        Output('fraud-rate', 'children'),
    ],
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_summary(selected_year, selected_month):
    filtered_df = df[(df['purchase_time'].dt.year == selected_year) & 
                     (df['purchase_time'].dt.strftime('%B') == selected_month)]
    total_txn = len(filtered_df)
    fraud_txn = filtered_df['class'].sum()  # Assuming 'class' = 1 means fraud
    fraud_rate = (fraud_txn / total_txn) * 100 if total_txn > 0 else 0
    return (
        f"{total_txn:,} Transactions",
        f"{fraud_txn:,} Fraudulent",
        f"{fraud_rate:.2f}% Fraud Rate"
    )

# Update Transactions Over Time Graph
@app.callback(
    Output('transactions-over-time', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_transactions_chart(selected_year, selected_month):
    filtered_df = df[(df['purchase_time'].dt.year == selected_year) & 
                     (df['purchase_time'].dt.strftime('%B') == selected_month)]
    fig = px.line(filtered_df, x='purchase_time', y='purchase_value',
                  title=f'Transactions Over Time - {selected_month} {selected_year}',
                  labels={'purchase_value': 'Transaction Amount (USD)'})
    fig.update_layout(xaxis_title='Date', yaxis_title='Amount')
    return fig

# Update Fraud Transaction Distribution Pie Chart
@app.callback(
    Output('fraud-pie-chart', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_fraud_pie(selected_year, selected_month):
    filtered_df = df[(df['purchase_time'].dt.year == selected_year) & 
                     (df['purchase_time'].dt.strftime('%B') == selected_month)]
    fraud_counts = filtered_df['class'].value_counts().reset_index()
    fraud_counts.columns = ['class', 'Count']
    fraud_counts['Label'] = fraud_counts['class'].map({1: 'Fraudulent', 0: 'Non-Fraudulent'})
    fig = px.pie(fraud_counts, names='Label', values='Count',
                 title=f'Fraud vs Non-Fraud Transactions - {selected_month} {selected_year}')
    return fig

# Update Transaction Count per User Bar Chart
@app.callback(
    Output('transaction-count-per-user', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_transaction_count_chart(selected_year, selected_month):
    filtered_df = df[(df['purchase_time'].dt.year == selected_year) & 
                     (df['purchase_time'].dt.strftime('%B') == selected_month)]
    txn_counts = filtered_df.groupby('user_id').size().reset_index(name='count')
    fig = px.bar(txn_counts, x='user_id', y='count',
                 title=f'Transaction Count Per User - {selected_month} {selected_year}',
                 labels={'count': 'Number of Transactions'})
    return fig

# Update Transaction Amount Histogram
@app.callback(
    Output('amount-distribution', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('month-dropdown', 'value')]
)
def update_amount_distribution(selected_year, selected_month):
    filtered_df = df[(df['purchase_time'].dt.year == selected_year) & 
                     (df['purchase_time'].dt.strftime('%B') == selected_month)]
    fig = px.histogram(filtered_df, x='purchase_value', nbins=50,
                       title=f'Transaction Amount Distribution - {selected_month} {selected_year}',
                       labels={'purchase_value': 'Transaction Amount (USD)'})
    fig.update_layout(yaxis_title='Frequency')
    return fig
