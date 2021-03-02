# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            Predict if the next month's close for the S&P 500 is up or down using a supervised learning model. 

            There is an enormous set of factors that go into making market predictions, and it is acknowledged that this app isn't the best at making them. 

            The S&P 500 - Month Ahead Direction application is to be used for fun, rather than for investment purposes.

            Is the market going to close up or down next month based on our inputs?  Let's find out!

            """
        ),
        dcc.Link(dbc.Button('Generate Predictions -->', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])