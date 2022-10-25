import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import dash_table 
import pandas as pd
import dash_bootstrap_components as dbc


CHART_THEME = 'plotly_dark'
external_stylesheets = [dbc.themes.DARKLY]

app = dash.Dash()

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([ 
            'darg and drop or',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=True
    ),
html.Div(id='output-data-upload'),

])

def parse_content(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8'))
            )
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([ 
            'There was an error processing this file.'
        ])
    return html.Div([ 
        dcc.Graph(
            fig = go.Figure(data=[
                go.Bar(name=df.columns.values[0], x=pd.unique(df['Name']), y=df['Fare'], text=df['Survival']),
            
            ])
            
            
        ),
    ])      

@app.callback(Output('output-data-upload', 'children'),
            [Input('upload-data', 'contents')],
            [State('upload-data', 'filename'),
            State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_content(c,n,d) for c,n,d in
            zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children

if __name__ == '__main__':
    app.run_server(debug=True)