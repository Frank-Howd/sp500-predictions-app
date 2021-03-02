# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load

pipeline = load("assets/XGBC.joblib")

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### 10-year Treasury (%)'),
        dcc.Slider(
            id='10-year-T',
            min=0.0,
            max=15.0,
            step=0.1,
            value=1.4,
            marks={n: str(n) for n in range(0,15,1)},
            className='mb-5'
        ),
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Quarterly Corporate Profits (Billions)'),
        dcc.Slider(
            id='Corporate-Profits',
            min=1500,
            max=3000,
            step=1,
            value=2200,
            marks={n: str(n) for n in range(1500,3000,150)},
            className='mb-5'
        ),
    ],
)

layout = dbc.Row([column1, column2])