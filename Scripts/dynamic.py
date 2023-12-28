import dash
import pyodbc
from dash import dcc,html
import plotly.graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc

app = dash.Dash()

server = 'TEST-DBASE1'
database = 'EazybankAX'
username = 'BIUser'
password = '1stepahead#'

# Connect to the SQL Server database
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=TEST-DBASE1;'
                      'DATABASE=EazybankAX;'
                      'Trusted_Connection=yes;')

# Create a cursor to execute queries
cursor = cnxn.cursor()
# Execute the query to fetch data for the bar chart
cursor.execute("select  b.RelationshipOfficerName as RelationshipOfficerName,count(*) as total,sum(a.Outstanding) as nplvalue as sum from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.Overdraft=1 group by b.RelationshipOfficerName order by count(*)")
bar_data = cursor.fetchall()

# Execute the query to fetch data for the pie chart
cursor.execute("select  b.RelationshipOfficerName as RelationshipOfficerName,count(*) as total,sum(CarryingAmount) as sum from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.Overdraft=1 group by b.RelationshipOfficerName order by count(*)")
pie_data = cursor.fetchall()

# Execute the query to fetch data for the scatter diagram
cursor.execute("select  b.RelationshipOfficerName as RelationshipOfficerName,count(*) as total,sum(CarryingAmount) as sum from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.Overdraft=1 group by b.RelationshipOfficerName order by count(*)")
scatter_data = cursor.fetchall()

# Execute the query to fetch data for marketer
cursor.execute("select distinct  RelationshipOfficerName as RelationshipOfficerName from VwAccMaster  where RelationshipOfficerName='Emmanuel, Sylvester'")
mname_data = cursor.fetchall()



# Execute the query to fetch data for the total npl accounts 
cursor.execute("select count(*) as tot from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and b.RelationshipOfficerName='Emmanuel, Sylvester ' and b.CreditClassDesc !='Performing' and  a.PostingDateAdded<='2022-12-31' group by b.RelationshipOfficerName order by count(*)")
nplacc_data = cursor.fetchall()


# Create a dictionary to store the data for the charts
data = {
    'bar': [go.Bar(x=[row[0] for row in bar_data], y=[row[1] for row in bar_data])],
    'pie': [go.Pie(labels=[row[0] for row in pie_data], values=[row[1] for row in pie_data])],
    'scatter': [go.Scatter(x=[row[0] for row in scatter_data], y=[row[1] for row in scatter_data])],
}
# Create a dictionary to store the data for cards visualisation
values = {
    'RelationshipOfficerName': mname_data[0][0],
    'nplacc':nplacc_data[0][0],
    
    
}
app.layout = html.Div(children=[
    html.H5(children='INFINITY TRUST MORTGAGE BANK',style={'color':'black','text-align':'center','background':'milk'}),
    html.H5(children='My Marketer Dashboard',style={'color':'black','text-align':'center'}),
    html.H5(children=f'NAME OF MARKETER: {values["RelationshipOfficerName"]}  |  TOTAL NUMBER OF OVERDRAFT LOANS : xxx |  DAILY DEPOSITS    : XXX |TOTAL NPL ACCOUNTS:{values["nplacc"]}   |   NPL VALUE :xxxx |  SALE OF HOUSE : XXX |  PROFITABILITY : XXX ',style={'color':'black','text-align':'center'}),
    html.Div(children=[
        
	html.H5(children=f'SUMMARY OF PERFORMANCE BY ALL MARKETERS')
	
    ]),
    dcc.Tabs(id='tabs', value='bar', children=[
        dcc.Tab(label='LOAN PORTFOLIO', value='bar', children=[
            dcc.Graph(
                id='bar-chart',
                figure={
                    'data': data['bar'],
                    'layout': {
                        'title': 'LOAN PORTFOLIO FOR ALL MARKETERS'
                    }
                }
            )
        ]),
        dcc.Tab(label='PERFORMANCE IN %', value='pie', children=[
            dcc.Graph(
                id='pie-chart',
                figure={
                    'data': data['pie'],
                    'layout': {
                        'title': 'PERFORMANCE IN %'
                    }
                }
            )
        ]),
        dcc.Tab(label='Scatter Diagram', value='scatter', children=[
            dcc.Graph(
                id='scatter-chart',
                figure={
                    'data': data['scatter'],
                    'layout': {
                        'title': 'Scatter Diagram'
                    }
                }
            )
        ])
    ])
])


if __name__ == '__main__':
    app.run_server(debug='true',host='10.2.2.50', port=8051)





































