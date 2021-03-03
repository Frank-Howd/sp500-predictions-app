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

# pipeline = load("assets/pipeline.joblib")
# pipeline = load("assets/XGBCfull.joblib")


@app.callback(
    Output('prediction-content', 'children'),
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
    return f'{y_pred[1]*100:.2f}% probability'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Add your predicted input values for the economic indicators presented on the right, 
            and  have the probability of the S&P 500 advancing in the following month 
            returned, based on these predictions. 

            """
        ),
        html.H3('________________________________', className='mb-3'), 
        html.H3('Percent chance next month close for the S&P 500 is up', className='mb-3'), 
        html.Div(id='prediction-content', className='lead')
    ],
    md=5,
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
            min=000,
            max=3500,
            step=1,
            value=2200,
            marks={n: str(n) for n in range(00,3501,500)},
            className='mb-5'
        ), 
        #dcc.Markdown('## Predictions', className='mb-5'),
        # dcc.Markdown('#### Consumer Price Index'),
        # dcc.Slider(
        #     id='CPI',
        #     min=100,
        #     max=400,
        #     step=1,
        #     value=285,
        #     marks={n: str(n) for n in range(100,401,50)},
        #     className='mb-5'
        # ), 
        #dcc.Markdown('## Predictions', className='mb-5'),
        # dcc.Markdown('#### Exports, Goods & Services (Billions)'),
        # dcc.Slider(
        #     id='Exports-Goods-Services',
        #     min=0,
        #     max=3000,
        #     step=10,
        #     value=2100,
        #     marks={n: str(n) for n in range(0,3001,500)},
        #     className='mb-5'
        # ), 
        #dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### U.S. Gross Domestic Product (Billions)'),
        dcc.Slider(
            id='GDP',
            min=5000,
            max=25000,
            step=1,
            value=19000,
            marks={n: str(n) for n in range(0,25001,2500)},
            className='mb-5'
        ),
        #dcc.Markdown('## Predictions', className='mb-5'),
        # dcc.Markdown('#### Housing Starts'),
        # dcc.Slider(
        #     id='Housing-Starts',
        #     min=0,
        #     max=3000,
        #     step=1,
        #     value=1487,
        #     marks={n: str(n) for n in range(0,3001,500)},
        #     className='mb-5'
        # ),
        #dcc.Markdown('## Predictions', className='mb-5'),
        # dcc.Markdown('#### Industrial Production Index'),
        # dcc.Slider(
        #     id='Industrial-Production',
        #     min=0,
        #     max=150,
        #     step=1,
        #     value=102,
        #     marks={n: str(n) for n in range(0,151,25)},
        #     className='mb-5'
        # ),
        #dcc.Markdown('## Predictions', className='mb-5'),
        # dcc.Markdown('#### Initial Claims'),
        # dcc.Slider(
        #     id='Initial-Claims',
        #     min=100_000,
        #     max=1_000_000,
        #     step=1_000,
        #     value=215_000,
        #     marks={n: str(n) for n in range(0,1_000_001,100_000)},
        #     className='mb-5'
        # ),
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