#!/usr/bin/env python
# coding: utf-8

# In[72]:


import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dbm
import plotly.graph_objs as go
import re
import dateutil
import pandas as pd

app = dash.Dash(__name__)
server = app.server

df = pd.read_csv(
    'BDPlus_Data_20190920.csv')


def generate_table(dataframe, max_rows=500):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


# In[73]:


df['Day'] = df['Date'].apply(dateutil.parser.parse, dayfirst=True)
df['Month'] = pd.DatetimeIndex(df['Day']).month
df['Year'] = pd.DatetimeIndex(df['Day']).year


# In[74]:


global sumDF
sumDF = df.groupby(['Name','Month','Year'], as_index=False)[['Points']].sum()


# In[80]:


global dict_names

def create_dict_list_of_names():
    dictlist = []
    unique_list = sumDF.Name.unique()
    for Name in unique_list:
        dictlist.append({'value': Name, 'label': Name})
    return dictlist

def dict_name_list(dict_list):
    name_list = []
    for dict in dict_list:
        name_list.append(dict.get('value'))
    return name_list

dict_names = create_dict_list_of_names()


# In[84]:


app.layout = html.Div([
    html.Div([
        html.H1('Proof of Concept - DASHboard'),
        html.H2('Choose a name'),
        dcc.Dropdown(
            id='name-dropdown',
            options=dict_names,
            multi=True,
            value = ["Anne Marie","Dave Smith"]
        ),
        dcc.Graph(
            id='Hours'
        )
    ], style={'width': '40%', 'display': 'inline-block'}),
    html.Div([
        html.H2('All Hours Info'),
        html.Table(id='full-table'),
        html.P(''),
    ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'}),
    html.Div([
        html.H2('Hours Graph'),
        dcc.Graph(id='hours-trend-graph'),
        html.P('')
    ], style={'width': '100%',  'display': 'inline-block'})

])


# In[85]:


@app.callback(Output('full-table', 'children'), [Input('name-dropdown', 'value')])
def generate_table(selected_dropdown_value, max_rows=20):
    sum_df_filter = sumDF[(sumDF['Name'].isin(selected_dropdown_value))]
    sum_df_filter = sum_df_filter.sort_values(['Name','Month'], ascending=True)
    
    return [html.Tr([html.Th(col) for col in sum_df_filter  .columns])] + [html.Tr([
        html.Td(sum_df_filter.iloc[i][col]) for col in sum_df_filter  .columns
    ]) for i in range(min(len(sum_df_filter  ), max_rows))]


# In[ ]:


if __name__ == '__main__':
    app.run_server(debug=True)

