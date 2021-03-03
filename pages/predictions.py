# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

# Imports from this application
from app import app
from joblib import load

pipeline = load("assets/XGBC.joblib")

sp = pd.read_csv('asset/sp500_df.csv')
target = 'SP500-PosNeg'
y = [target]
X = sp.drop(columns=target)
pipeline.fit(X, y)

@app.callback(
    Output('prediction-content', 'SP500-PosNeg'),
    [Input('10-year-T', 'value'),
     Input('Corporate-Profits', 'value'),
     Input('GDP', 'value'),
     Input('Net-Exports', 'value'),
     Input('Unemployment-Rate', 'value')],
)
def predict(ten_year, corporate_profits, gdp, net_exports, unemployment):
    df = pd.DataFrame(
        columns=['10-yr-Treasury', 
                 'Corporate-Profits', 
                 'GDP',
                 'Net-Exports',
                 'Unemployment_Rate'],
        data=[[ten_year, corporate_profits, gdp, net_exports, unemployment]]
    )
    y_pred = pipeline.predict_proba(df)[0]
    return f'{y_pred} years'

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
        html.H2('Percent chance next month close for the S&P 500 is up', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        #dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### 10-year Treasury (%)'),
        dcc.Slider(
            id='10-year-T',
            min=0.0,
            max=16.0,
            step=0.1,
            value=1.4,
            marks={n: str(n) for n in range(0,17,2)},
            className='mb-5'
        ),
        #dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Corporate Profits (Billions)'),
        dcc.Slider(
            id='Corporate-Profits',
            min=1300,
            max=3200,
            step=1,
            value=2200,
            marks={n: str(n) for n in range(1500,3100,300)},
            className='mb-5'
        ),
        #dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### U.S. Gross Domestic Product (Billions)'),
        dcc.Slider(
            id='GDP',
            min=5000,
            max=22000,
            step=1,
            value=19000,
            marks={n: str(n) for n in range(7000,21000,3000)},
            className='mb-5'
        ),
        #dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Net Exports (Billions)'),
        dcc.Slider(
            id='Net-Exports',
            min=-1000,
            max=500,
            step=10,
            value=-740,
            marks={n: str(n) for n in range(-1000,1000,250)},
            className='mb-5'
        ),
        #dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Unemployment Rate (%)'),
        dcc.Slider(
            id='Unemployment-Rate',
            min=0.0,
            max=16.0,
            step=0.1,
            value=6.3,
            marks={n: str(n) for n in range(0,17,2)},
            className='mb-5'
        )
    ]
)

layout = dbc.Row([column1, column2])