import dash
from dash import dcc, html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
from q import *

app = dash.Dash(__name__)
server = app.server

df_real_assets =pd.read_csv("data/df_real_assets.csv")

app.layout = html.Div([
    html.Div(
        html.Div(dcc.Dropdown(
            id="Dropdown-symbols",
            options=[
            {'label': i, 'value': i} for i in df_real_assets.symbol.unique()
        ],
        value='UTMCLP'),
        style={'width': '50%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),

    html.Br(),
        html.Div(
            html.Div(dcc.Graph(id='my-output'),
            style={'width': '70%'}),
    style={ 'display': 'flex', 'justify-content': 'center'}),
])
@app.callback(
    Output('my-output','figure'),
    Input('Dropdown-symbols', 'value'))

def update_output_div(input_value):
    row = df_real_assets[df_real_assets.symbol==input_value]
    id = row.id.values
    start_date = row.start_date.values
    end_date = row.end_date.values
    
    df_real_assets_days = plot_data(start_date[0],end_date[0],id[0])

    fig = px.line(df_real_assets_days, x="date", y="price")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)