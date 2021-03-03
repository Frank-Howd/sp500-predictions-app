# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights from Data Visualizations


            """
        ),
        html.H3('______________________________________________', className='mb-3'), 
        html.H5('Correlation is high between many of the features and the target.', className='mb-3'), 
        dcc.Markdown(
            """
        
            * GDP

            * CPI

            * Exports of goods & services

            * Industrial production

            * Corporate profits

            """
        ), 
        html.H3('______________________________________________', className='mb-3'), 
        html.H5('Correlation is also high between many of the explanatory variables - multicollinearity.', className='mb-3'), 
        dcc.Markdown(
            """
        
            * Corporate profits

            * CPI
            
            * GDP
            
            * Exports of goods & services
            
            * Industrial production
            
            """
        ),
        dcc.Markdown(
            """
        
            The coefficient estimates may change erratically to small changes in the model or the data. 
            
            """
        ),
        dcc.Markdown(
            """
            
            * It affects calculations regarding individual predictors.

            """
        ),
         dcc.Markdown(
            """
            
            * The model may or may not perform well. 

            """
        ),
        html.H3('______________________________________________', className='mb-3'), 
        html.H5("Useful signaling between features and target isn't always easy to find", className='mb-3'), 
        dcc.Markdown(
            """
        
            * Pockets of directional trends

            * Periods without directional preference
            
            * From 1985 through approximately 1997, the 'trend was your friend'
            
            * From 1998 through approximately 2002 the market advanced/declined
            
            * But 1998 through approximately 2002 also showed listless corporate profits
 
            * Following 2002 we can some directional synergy, albeit with different force velocities

            * Random walk or useful input?
            
            """
        ),
        dcc.Markdown(
            """
            
            Hold times matter, and long-term trends save most index investors in the end,

            """
        ),
        dcc.Markdown(
            """
            
            ...as long as they hold on for dear life ---> the longer the better.

            """
        ), 
        html.H3('______________________________________________', className='mb-3'), 
        html.H5("Distributions of the Feature Variables", className='mb-3'), 
        dcc.Markdown(
            """
        
            * Varied in presentation

            * Most variable distributions were non-monotonic.
            
            * Some outliers were present in the data

            * Log transformations did not appear to reign in the data spreads for this dataset
            
            * Examination of variables over a longer time-period would be preferred
            
            """
        ),
        html.H3('______________________________________________', className='mb-3'), 
        html.H5("Quick scatter plotting of the features versus the target", className='mb-3'), 
        dcc.Markdown(
            """
              
            * Connections were often seemingly apparent

            * Outliers are present 
            
            * OLS appears biased 

            * Another take on random walk versus useful ignal generating input
            
            """
        ),
        html.H3('______________________________________________', className='mb-3'), 
        html.H5("PDP Isolate Plots and PDP Interact Plots", className='mb-3'), 
        dcc.Markdown(
            """
        
            * PDP isolate plots show the marginal effects a feature has on the predicted outcome

            * The isolate plot on the right shows us that declines in industrial production decrease the chances of the index advancing
            
            * PDP interact plot shows us the marginal effect that two features have on the predicted model outcome

            * The interact plot on the lower right tells us that as long-term interest rates rise, the probability of the index advancing decreases

            * The interact plot also indicates that as corporate profits increase, so do the chances of the market advancing in the following month
            
            """
        ),        
    ],
    md=7
)

column2 = dbc.Col(
    [
        html.Img(src='assets/target_correlation.png', className='img-fluid'),
        html.Img(src='assets/heatmap_features.png', className='img-fluid'),
        html.Img(src='assets/cp_sp.png', className='img-fluid'),
        html.Img(src='assets/histogram.png', className='img-fluid'),
        html.Img(src='assets/regression.png', className='img-fluid'),
        html.Img(src='assets/ind_prod.png', className='img-fluid'),
        html.Img(src='assets/pdp_interact_2D.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])