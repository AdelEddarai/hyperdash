from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

# Instantiates our app and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


# colors
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


# incorporate data into app
df = px.data.gapminder()
print(df.head())

# Build the scatter plot
fig = px.scatter(data_frame=df, x="gdpPercap", y="lifeExp", size="pop",
                color="continent", hover_name="country", log_x=True,
                size_max=60, range_y=[30, 90], animation_frame='year')

# Build the layout to define what will be displayed on the page
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("life expectancy vs GDP", style={'textAlign': 'center', 'color': colors['text']}),
            html.Div(style={'backgroundColor': colors['background']})
        ], width=10)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='our-plot', figure=fig, style={'plot_bgcolor': colors['background'], 'plot_bgcolor': colors['background']})
        ], width=12)

    ]),

    dbc.Row([
        dbc.Col([
            html.Label('Dropdown'),
            dcc.Dropdown(options=[x for x in df.year.unique()],
                        value=df.year[0]),
        ], width=6)
    ])

])
 # callback is used to create app interactivity
 # @callback()

if __name__ == '__main__':
	app.run_server(debug=True)