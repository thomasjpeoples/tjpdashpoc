#!/usr/bin/env python
# coding: utf-8

# In[90]:


import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dbm
import plotly.graph_objs as go
import re
import dateutil
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


# In[95]:


#df = pd.read_csv('BDPlus_Data_20190920.csv')
rawdata = [
['22/09/2019','Weekly Core Hours',10,'Dave Smith'],
['22/09/2019','Weekly Additional Hours',2,'Dave Smith'],
['15/09/2019','Weekly Core Hours',10,'Dave Smith'],
['15/09/2019','Weekly Core Hours',10,'Dave Smith'],
['08/09/2019','Weekly Core Hours',10,'Dave Smith'],
['08/09/2019','Weekly Core Hours',10,'Dave Smith'],
['01/09/2019','Weekly Core Hours',10,'Dave Smith'],
['01/09/2019','Weekly Core Hours',10,'Dave Smith'],
['25/08/2019','Weekly Core Hours',10,'Dave Smith'],
['25/08/2019','Weekly Core Hours',10,'Dave Smith'],
['18/08/2019','Weekly Core Hours',10,'Dave Smith'],
['18/08/2019','Weekly Core Hours',10,'Dave Smith'],
['11/08/2019','Weekly Core Hours',10,'Dave Smith'],
['11/08/2019','Weekly Core Hours',10,'Dave Smith'],
['04/08/2019','Weekly Core Hours',10,'Dave Smith'],
['04/08/2019','Weekly Core Hours',10,'Dave Smith'],
['28/07/2019','Weekly Core Hours',10,'Dave Smith'],
['28/07/2019','Weekly Core Hours',10,'Dave Smith'],
['21/07/2019','Weekly Core Hours',10,'Dave Smith'],
['21/07/2019','Weekly Core Hours',10,'Dave Smith'],
['14/07/2019','Weekly Core Hours',10,'Dave Smith'],
['14/07/2019','Weekly Core Hours',10,'Dave Smith'],
['07/07/2019','Weekly Core Hours',10,'Dave Smith'],
['07/07/2019','Weekly Core Hours',10,'Dave Smith'],
['30/06/2019','Weekly Core Hours',10,'Dave Smith'],
['30/06/2019','Weekly Core Hours',10,'Dave Smith'],
['23/06/2019','Weekly Core Hours',10,'Dave Smith'],
['23/06/2019','Weekly Additional Hours',2,'Dave Smith'],
['16/06/2019','Weekly Additional Hours',2,'Dave Smith'],
['16/06/2019','Weekly Additional Hours',2,'Dave Smith'],
['09/06/2019','Weekly Additional Hours',2,'Dave Smith'],
['09/06/2019','Weekly Additional Hours',2,'Dave Smith'],
['02/06/2019','Weekly Additional Hours',2,'Dave Smith'],
['02/06/2019','Weekly Additional Hours',2,'Dave Smith'],
['26/05/2019','Weekly Additional Hours',2,'Dave Smith'],
['26/05/2019','Weekly Additional Hours',2,'Dave Smith'],
['19/05/2019','Weekly Additional Hours',2,'Dave Smith'],
['19/05/2019','Weekly Additional Hours',2,'Dave Smith'],
['12/05/2019','Weekly Additional Hours',2,'Dave Smith'],
['12/05/2019','Weekly Additional Hours',2,'Dave Smith'],
['05/05/2019','Weekly Additional Hours',2,'Dave Smith'],
['05/05/2019','Weekly Additional Hours',2,'Dave Smith'],
['28/04/2019','Weekly Additional Hours',2,'Dave Smith'],
['28/04/2019','Weekly Additional Hours',2,'Dave Smith'],
['21/04/2019','Weekly Additional Hours',2,'Dave Smith'],
['21/04/2019','Weekly Additional Hours',2,'Dave Smith'],
['14/04/2019','Weekly Additional Hours',2,'Dave Smith'],
['14/04/2019','Weekly Additional Hours',2,'Dave Smith'],
['07/04/2019','Weekly Additional Hours',2,'Dave Smith'],
['07/04/2019','Weekly Additional Hours',2,'Dave Smith'],
['31/03/2019','Weekly Additional Hours',2,'Dave Smith'],
['31/03/2019','Weekly Additional Hours',2,'Dave Smith'],
['31/03/2019','Weekly Core Hours',15,'Anne Marie'],
['31/03/2019','Weekly Additional Hours',7,'Anne Marie'],
['07/04/2019','Weekly Core Hours',15,'Anne Marie'],
['14/04/2019','Weekly Core Hours',15,'Anne Marie'],
['21/04/2019','Weekly Core Hours',15,'Anne Marie'],
['28/04/2019','Weekly Core Hours',15,'Anne Marie'],
['05/05/2019','Weekly Core Hours',15,'Anne Marie'],
['12/05/2019','Weekly Core Hours',15,'Anne Marie'],
['19/05/2019','Weekly Core Hours',15,'Anne Marie'],
['26/05/2019','Weekly Core Hours',15,'Anne Marie'],
['02/06/2019','Weekly Core Hours',15,'Anne Marie'],
['09/06/2019','Weekly Core Hours',15,'Anne Marie'],
['16/06/2019','Weekly Core Hours',15,'Anne Marie'],
['23/06/2019','Weekly Core Hours',15,'Anne Marie'],
['30/06/2019','Weekly Core Hours',15,'Anne Marie'],
['07/07/2019','Weekly Core Hours',15,'Anne Marie'],
['14/07/2019','Weekly Core Hours',15,'Anne Marie'],
['21/07/2019','Weekly Core Hours',15,'Anne Marie'],
['28/07/2019','Weekly Core Hours',15,'Anne Marie'],
['04/08/2019','Weekly Core Hours',15,'Anne Marie'],
['11/08/2019','Weekly Core Hours',15,'Anne Marie'],
['18/08/2019','Weekly Core Hours',15,'Anne Marie'],
['25/08/2019','Weekly Core Hours',15,'Anne Marie'],
['01/09/2019','Weekly Core Hours',15,'Anne Marie'],
['08/09/2019','Weekly Core Hours',15,'Anne Marie'],
['15/09/2019','Weekly Core Hours',15,'Anne Marie'],
['22/09/2019','Weekly Core Hours',15,'Anne Marie'],
['07/04/2019','Weekly Additional Hours',7,'Anne Marie'],
['14/04/2019','Weekly Additional Hours',7,'Anne Marie'],
['21/04/2019','Weekly Additional Hours',7,'Anne Marie'],
['28/04/2019','Weekly Additional Hours',7,'Anne Marie'],
['05/05/2019','Weekly Additional Hours',7,'Anne Marie'],
['12/05/2019','Weekly Additional Hours',7,'Anne Marie'],
['19/05/2019','Weekly Additional Hours',7,'Anne Marie'],
['26/05/2019','Weekly Additional Hours',7,'Anne Marie'],
['02/06/2019','Weekly Additional Hours',7,'Anne Marie'],
['09/06/2019','Weekly Additional Hours',7,'Anne Marie'],
['16/06/2019','Weekly Additional Hours',7,'Anne Marie'],
['23/06/2019','Weekly Additional Hours',7,'Anne Marie'],
['30/06/2019','Weekly Additional Hours',7,'Anne Marie'],
['07/07/2019','Weekly Additional Hours',7,'Anne Marie'],
['14/07/2019','Weekly Additional Hours',7,'Anne Marie'],
['21/07/2019','Weekly Additional Hours',7,'Anne Marie'],
['28/07/2019','Weekly Additional Hours',7,'Anne Marie'],
['04/08/2019','Weekly Additional Hours',7,'Anne Marie'],
['11/08/2019','Weekly Additional Hours',7,'Anne Marie'],
['18/08/2019','Weekly Additional Hours',7,'Anne Marie'],
['25/08/2019','Weekly Additional Hours',7,'Anne Marie'],
['01/09/2019','Weekly Additional Hours',7,'Anne Marie'],
['08/09/2019','Weekly Additional Hours',7,'Anne Marie'],
['15/09/2019','Weekly Additional Hours',7,'Anne Marie'],
['22/09/2019','Weekly Additional Hours',7,'Anne Marie'],
['31/03/2019','Weekly Core Hours',12,'John Doe'],
['05/05/2019','Weekly Additional Hours',8,'John Doe'],
['28/04/2019','Weekly Core Hours',12,'John Doe'],
['21/04/2019','Weekly Core Hours',12,'John Doe'],
['14/04/2019','Weekly Core Hours',12,'John Doe'],
['07/04/2019','Weekly Core Hours',12,'John Doe'],
['31/03/2019','Weekly Core Hours',12,'John Doe'],
['12/05/2019','Weekly Core Hours',12,'John Doe'],
['19/05/2019','Weekly Core Hours',12,'John Doe'],
['26/05/2019','Weekly Core Hours',12,'John Doe'],
['02/06/2019','Weekly Core Hours',12,'John Doe'],
['09/06/2019','Weekly Core Hours',12,'John Doe'],
['16/06/2019','Weekly Core Hours',12,'John Doe'],
['23/06/2019','Weekly Core Hours',12,'John Doe'],
['30/06/2019','Weekly Core Hours',12,'John Doe'],
['07/07/2019','Weekly Core Hours',12,'John Doe'],
['14/07/2019','Weekly Core Hours',12,'John Doe'],
['22/09/2019','Weekly Core Hours',12,'John Doe'],
['15/09/2019','Weekly Core Hours',12,'John Doe'],
['08/09/2019','Weekly Core Hours',12,'John Doe'],
['01/09/2019','Weekly Core Hours',12,'John Doe'],
['25/08/2019','Weekly Core Hours',12,'John Doe'],
['18/08/2019','Weekly Core Hours',12,'John Doe'],
['11/08/2019','Weekly Core Hours',12,'John Doe'],
['04/08/2019','Weekly Core Hours',12,'John Doe'],
['28/07/2019','Weekly Core Hours',12,'John Doe'],
['21/07/2019','Weekly Core Hours',12,'John Doe'],
['07/04/2019','Weekly Additional Hours',8,'John Doe'],
['14/04/2019','Weekly Additional Hours',8,'John Doe'],
['21/04/2019','Weekly Additional Hours',8,'John Doe'],
['28/04/2019','Weekly Additional Hours',8,'John Doe'],
['05/05/2019','Weekly Additional Hours',8,'John Doe'],
['12/05/2019','Weekly Additional Hours',8,'John Doe'],
['19/05/2019','Weekly Additional Hours',8,'John Doe'],
['26/05/2019','Weekly Additional Hours',8,'John Doe'],
['02/06/2019','Weekly Additional Hours',8,'John Doe'],
['09/06/2019','Weekly Additional Hours',8,'John Doe'],
['16/06/2019','Weekly Additional Hours',8,'John Doe'],
['23/06/2019','Weekly Additional Hours',8,'John Doe'],
['30/06/2019','Weekly Additional Hours',8,'John Doe'],
['07/07/2019','Weekly Additional Hours',8,'John Doe'],
['14/07/2019','Weekly Additional Hours',8,'John Doe'],
['21/07/2019','Weekly Additional Hours',8,'John Doe'],
['28/07/2019','Weekly Additional Hours',8,'John Doe'],
['04/08/2019','Weekly Additional Hours',8,'John Doe'],
['11/08/2019','Weekly Additional Hours',8,'John Doe'],
['18/08/2019','Weekly Additional Hours',8,'John Doe'],
['25/08/2019','Weekly Additional Hours',8,'John Doe'],
['01/09/2019','Weekly Additional Hours',8,'John Doe'],
['08/09/2019','Weekly Additional Hours',8,'John Doe'],
['15/09/2019','Weekly Additional Hours',8,'John Doe'],
['22/09/2019','Weekly Additional Hours',8,'John Doe'],
['31/03/2019','Weekly Core Hours',6,'Mary Jane'],
['31/03/2019','Weekly Additional Hours',8,'Mary Jane'],
['07/04/2019','Weekly Core Hours',6,'Mary Jane'],
['14/04/2019','Weekly Core Hours',6,'Mary Jane'],
['21/04/2019','Weekly Core Hours',6,'Mary Jane'],
['28/04/2019','Weekly Core Hours',6,'Mary Jane'],
['05/05/2019','Weekly Core Hours',6,'Mary Jane'],
['12/05/2019','Weekly Core Hours',6,'Mary Jane'],
['19/05/2019','Weekly Core Hours',6,'Mary Jane'],
['26/05/2019','Weekly Core Hours',6,'Mary Jane'],
['02/06/2019','Weekly Core Hours',6,'Mary Jane'],
['09/06/2019','Weekly Core Hours',6,'Mary Jane'],
['16/06/2019','Weekly Core Hours',6,'Mary Jane'],
['23/06/2019','Weekly Core Hours',6,'Mary Jane'],
['30/06/2019','Weekly Core Hours',6,'Mary Jane'],
['07/07/2019','Weekly Core Hours',6,'Mary Jane'],
['14/07/2019','Weekly Core Hours',6,'Mary Jane'],
['22/09/2019','Weekly Core Hours',6,'Mary Jane'],
['15/09/2019','Weekly Core Hours',6,'Mary Jane'],
['08/09/2019','Weekly Core Hours',6,'Mary Jane'],
['01/09/2019','Weekly Core Hours',6,'Mary Jane'],
['25/08/2019','Weekly Core Hours',6,'Mary Jane'],
['18/08/2019','Weekly Core Hours',6,'Mary Jane'],
['11/08/2019','Weekly Core Hours',6,'Mary Jane'],
['04/08/2019','Weekly Core Hours',6,'Mary Jane'],
['28/07/2019','Weekly Core Hours',6,'Mary Jane'],
['21/07/2019','Weekly Core Hours',6,'Mary Jane'],
['02/06/2019','Weekly Additional Hours',8,'Mary Jane'],
['26/05/2019','Weekly Additional Hours',8,'Mary Jane'],
['19/05/2019','Weekly Additional Hours',8,'Mary Jane'],
['12/05/2019','Weekly Additional Hours',8,'Mary Jane'],
['05/05/2019','Weekly Additional Hours',8,'Mary Jane'],
['28/04/2019','Weekly Additional Hours',8,'Mary Jane'],
['21/04/2019','Weekly Additional Hours',8,'Mary Jane'],
['14/04/2019','Weekly Additional Hours',8,'Mary Jane'],
['07/04/2019','Weekly Additional Hours',8,'Mary Jane'],
['09/06/2019','Weekly Additional Hours',8,'Mary Jane'],
['16/06/2019','Weekly Additional Hours',8,'Mary Jane'],
['23/06/2019','Weekly Additional Hours',8,'Mary Jane'],
['30/06/2019','Weekly Additional Hours',8,'Mary Jane'],
['07/07/2019','Weekly Additional Hours',8,'Mary Jane'],
['14/07/2019','Weekly Additional Hours',8,'Mary Jane'],
['21/07/2019','Weekly Additional Hours',8,'Mary Jane'],
['28/07/2019','Weekly Additional Hours',8,'Mary Jane'],
['04/08/2019','Weekly Additional Hours',8,'Mary Jane'],
['11/08/2019','Weekly Additional Hours',8,'Mary Jane'],
['18/08/2019','Weekly Additional Hours',8,'Mary Jane'],
['25/08/2019','Weekly Additional Hours',8,'Mary Jane'],
['01/09/2019','Weekly Additional Hours',8,'Mary Jane'],
['08/09/2019','Weekly Additional Hours',8,'Mary Jane'],
['15/09/2019','Weekly Additional Hours',8,'Mary Jane'],
['22/09/2019','Weekly Additional Hours',8,'Mary Jane']
]

df = pd.DataFrame(rawdata, columns = ['Date', 'Description','Points','Name']) 


# In[ ]:


def generate_table(dataframe, max_rows=500):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


# In[91]:


df['Day'] = df['Date'].apply(dateutil.parser.parse, dayfirst=True)
df['Month'] = pd.DatetimeIndex(df['Day']).month
df['Year'] = pd.DatetimeIndex(df['Day']).year


# In[92]:


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
            id='name-like-bar'
        )
    ], style={'width': '40%', 'display': 'inline-block'}),
    html.Div([
        html.H2('All Points Info'),
        html.Table(id='full-table'),
        html.P(''),
    ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'}),
    html.Div([
        html.H2('Points Graph'),
        dcc.Graph(id='points-trend-graph'),
        html.P('')
    ], style={'width': '100%',  'display': 'inline-block'})

])


# In[89]:


@app.callback(Output('name-like-bar', 'figure'), [Input('name-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    name_df_filter = sumDF[(sumDF['Name'].isin(selected_dropdown_value))]

    name_df_filter = name_df_filter.sort_values('Month', ascending=False)

    figure = {
        'data': [go.Bar(
            y=name_df_filter.Points,
            x=name_df_filter.Name,
            orientation='v'
        )],
        'layout':go.Layout(
            title= 'Name Rating Trends',
            yaxis = dict(
                # autorange=True,
                automargin=True
            )
        )
    }
    return figure


# In[ ]:


# For the top topics graph
@app.callback(Output('points-trend-graph', 'figure'), [Input('name-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    name_df_filter = sumDF[(sumDF['Name'].isin(selected_dropdown_value))]

    data = timeline_name_filtered(name_df_filter,selected_dropdown_value)
    # Edit the layout
    layout = dict(title='Points Accumulated Over Time',
                  xaxis=dict(title='Month'),
                  yaxis=dict(title='Points'),
                  )
    figure = dict(data=data,layout=layout)
    return figure

def timeline_name_filtered(top_name_filtered_df, selected_dropdown_value):
    # Make a timeline
    trace_list = []
    for value in selected_dropdown_value:
        top_name_value_df = top_name_filtered_df[top_name_filtered_df['Name']==value]
        trace = go.Scatter(
            y=top_name_value_df.Points,
            x=top_name_value_df.Month,
            name = value
        )
        trace_list.append(trace)
    return trace_list


# In[85]:


# for the table
@app.callback(Output('full-table', 'children'), [Input('name-dropdown', 'value')])
def generate_table(selected_dropdown_value, max_rows=20):
    name_df_filter = sumDF[(sumDF['Name'].isin(selected_dropdown_value))]
    name_df_filter = name_df_filter.sort_values(['Name','Month'], ascending=True)
    
    return [html.Tr([html.Th(col) for col in name_df_filter  .columns])] + [html.Tr([
        html.Td(name_df_filter.iloc[i][col]) for col in name_df_filter  .columns
    ]) for i in range(min(len(name_df_filter  ), max_rows))]


# In[ ]:


if __name__ == '__main__':
    app.run_server(debug=True)

