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

        html.Img(src='assets/sp_index.png', className='img-fluid'), 
        dcc.Markdown(
            """
        
            ## Where Do We Go From Here???


            """
        ),
        dcc.Markdown(
            """
        
            I have a passion for bottoms up investing. I look at companies one at a time, read annual reports, 
            build out integrated financial statement models to determine long rate capital expenditures and 
            earnings, examine returns on invested capital, understand the capital structure, discount projected 
            future cash flows, and ultimately arrive at an estimation of value, or an expected internal rate-of-return 
            for the going concern. I love this stuff. I consider Stephen Penman from Columbia University, 
            Aswath Demodaran from NYU Stern, and Warren Buffett as true sources of inspiration for these 
            endeavors. 

            """
        ),
        dcc.Markdown(
            """
        
            So for this project, I was curious to look at things from another perspective - a top down, 
            bird's eye view of the stock market- macro versus micro. I wanted to examine supervised machine 
            learning in action. My goal was to source and build out a simple dataset of economic indicators, 
            work with the data, and build out some models to assess their predictive performance. The question 
            I wanted to answer was, "Will the following month's close for the S&P 500 be up or down?"

            """
        ),
        dcc.Markdown(
            """
        
            Baseline accuracy for the period observed was 62.93% - the frequency that the S&P 500 closed higher. 
            Could we beat the baseline?

            """
        ),
        dcc.Markdown(
            """
        
            So deceptively simple is that previous sentence. As anyone who has already explored these types of 
            models already knows, I definitely ran into trouble during my first dives into the world of index 
            forecasting.

            """
        ),
        dcc.Markdown(
            """
        
            Baseline accuracy for the period observed was 62.93% - the frequency that the S&P 500 closed higher. 
            Could we beat the baseline?

            """
        ),
        dcc.Markdown(
            """
        
            My first troubles lied in gathering good data. I needed data that would travel far enough back in 
            the past to yield sufficient observations for creating a useful supervised machine learning model. 
            Items like U.S. gross domestic product and corporate profits are indicated on a quarterly basis, while 
            initial unemployment claims and long-term interest rates are tracked daily. Some of the indicators 
            I sourced are only measured since the 1980s. I ended up gathering as many monthly data points as able for 
            10 features plus a target- and I thank the Federal Reserve of St. Louis for the bulk of this information. 
            S&P 500 index levels were sourced from Yahoo Finance. Using monthly data (and forward fills for quarterly 
            data), I was able to go back in time through 1985, which sounds like a lot but only yielded 427 observations. 
            I ended up with a small dataset, but not necessarily an uncommon sizing for these types of projects either.

            """
        ),
        dcc.Markdown(
            """
        
            After adjusting the S&P 500 close back by a month, I had the computer do some basic math, and created a 
            binary target column - S&P 500 up or down. Then I started some exploratory data analysis with some plotting.

            """
        ),
        dcc.Markdown(
            """
        
            * Many of the feature variables were highly correlated to the target.

            """
        ),
        dcc.Markdown(
            """
        
            * Some quickly graphed scatter plots looked like they had high bias.

            """
        ),
        dcc.Markdown(
            """
        
           * There were times when feature signal appeared directionless.

            """
        ),
        dcc.Markdown(
            """
        
            * Most of the feature distributions were non-monotonic.

            """
        ),
        dcc.Markdown(
            """
        
            * Many features were also highly correlated with each other, suggesting the presence of 
            multicollinearity.
    

            """
        ),
        dcc.Markdown(
            """
        
            It was possible that the models would change erratically in response to small changes in the 
            model or the data - spoiler alert, they definitely didn't perform well.

            """
        ),
        dcc.Markdown(
            """
        
            After some feature exploring, adjusting, and engineering, four models were constructed - a 
            Logistic Regression model, a Random Forest Classifier, a Ridge Classifier and a XGBoost Classifier. 
            All models were either tuned using a RandomizedSearchCV, a GridSearchCV, or hand tuned using 
            validation curves.

            """
        ),
        dcc.Markdown(
            """
        
            PDP isolate plots were created to see how the target was influenced by the features in isolation.  
            PDP interact plots, and 3D PDP interact plots, were also created to examine the effects of multiple 
            features, in concert, on the target.  Finally, Shap plots were explored, to gather additional 
            information about how a model arrived at individual predictions.

            """
        ),
        html.Img(src='assets/shap_plot.png', className='img-fluid'),
        dcc.Markdown(
            """
        
            At the end of it all, despite all of this exploration, data wrangling, and tuning, the model scores were not much better 
            than always just guessing that the next month's market close would be up. All of the models finished with an accuracy of 
            around 68 percent on their test sets.

            """
        ),
        dcc.Markdown(
            """
        
            But this doesn't truly inform of how bad these models truly performed.

            """
        ),
        dcc.Markdown(
            """
        
            The only model that didn't say the market would move directionally upwards in the month ahead for every 
            single observation in the test set was the XGBoost XGBClassifier.

            """
        ),
        dcc.Markdown(
            """
        
            Quite the recall, but you can't miss the absolute lack of precision either.

            """
        ),
        dcc.Markdown(
            """
        
            And the ROC-AUC curves for the models? Oopha. 
            The models performed, collectively, no better than flipping a coin to generate a prediction.

            """
        ),
        dcc.Markdown(
            """
        
            So where are we now? Perhaps surprisingly, undiscouraged. It should be pretty obvious that supervised 
            machine learning is a challenging method to apply for the generation of accurate stock market predictions, 
            even when presented as a simple binary classification problem. I wouldn't be making trades with these models, 
            but I will continue to explore and expand my learning. I will continue to learn how to generate effective predictive 
            financial market models and I will continue to discover where to gather good data. I will continue to spend time 
            learning how to generate appropriate predictive signals with feature creation, model selection, and model tuning. 
            I will need to learn how to more effectively address multicollinearity in my models. I will need to be able to access 
            data that travels back further in time, so that my dataset appropriately lengthen while it widens. Ultimately, it is 
            as the saying goes though, "You've gotta start somewhere." And from how these models performed, it also appears safe to say, 
            "Things will only be getting better from here." I am excited.
            """
        ),
    ],
)

layout = dbc.Row([column1])