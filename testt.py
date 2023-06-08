import dash
import pyodbc
from dash import dcc
from dash import html
import plotly.graph_objs as go
app = dash.Dash()

# Connect to the SQL Server database
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=TEST-DBASE1;'
                      'DATABASE=EazybankAX1;'
                      'Trusted_Connection=yes;')

# Create a cursor to execute queries
cursor = cnxn.cursor()

# Execute the query to fetch data for the bar chart-LOANS
cursor.execute("select a.AccountDesc as accountName,a.AmountGranted  as amountgranted from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.CreditTypeDesc='Mortgage Loan' and a.PostingDateAdded between '2023-01-01' and '2023-12-01' and RelationshipOfficerName in('OKAFOR, ERIC UCHENNA')")
bar_data = cursor.fetchall()

# Execute the query to fetch data for the pie chart-pbt
query ="select sum(a.AmountGranted)   from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.CreditTypeDesc='Mortgage Loan' and a.PostingDateAdded between '2023-01-01' and '2023-12-31' and RelationshipOfficerName in('OKAFOR, ERIC UCHENNA')"
cursor = cnxn.cursor()
cursor.execute(query)
progress = cursor.fetchone()[0]
# update the `pie_data` list with the retrieved progress   
pbt_data = [('SET TARGET',   113373000.00), ('ACHIEVED TARGET', progress)]
# Specify colors for pie chart slices
colors = ['#00203FFF','#ADEFD1FF']  # green for SET TARGET, red for ACHIEVED TARGET

# Execute the query to fetch data for the pie chart-sale of house
query ="select sum(a.AmountGranted)   from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.CreditTypeDesc='Mortgage Loan' and a.PostingDateAdded between '2023-01-01' and '2023-12-31' and RelationshipOfficerName in('OKAFOR, ERIC UCHENNA')"
cursor = cnxn.cursor()
cursor.execute(query)
progress = cursor.fetchone()[0]
# update the `pie_data` list with the retrieved progress   
soh_data = [('SET TARGET',   37109583.55), ('ACHIEVED TARGET', progress)]
# Specify colors for pie chart slices
colors = ['#00203FFF','#ADEFD1FF']  # green for SET TARGET, red for ACHIEVED TARGET

# Execute the query to fetch data for the pie chart-target(loans)
query ="select sum(a.AmountGranted)   from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.CreditTypeDesc='Mortgage Loan' and a.PostingDateAdded between '2023-01-01' and '2023-12-31' and RelationshipOfficerName in('OKAFOR, ERIC UCHENNA')"
cursor = cnxn.cursor()
cursor.execute(query)
progress = cursor.fetchone()[0]
# update the `pie_data` list with the retrieved progress   
pie_data = [('SET TARGET',  1326000000.00 ), ('ACHIEVED TARGET', progress)]
# Specify colors for pie chart slices
colors = ['#00203FFF','#ADEFD1FF']  # green for SET TARGET, red for ACHIEVED TARGET

# Execute the query to fetch data for the pie chart2-target(deposits)
query2 ="select sum(a.BalAcctCurr) from VwTransHist a,VwAccMaster b where a.AccountNo=b.AccountNo and TransCode in('103','1031') and a.PostingDateAdded between '2023-01-01' and '2023-12-31' and  RelationshipOfficerName in('OKAFOR, ERIC UCHENNA')"
cursor2 = cnxn.cursor()
cursor2.execute(query2)
progress2 = cursor2.fetchone()[0]
# update the `pie_data` list with the retrieved progress   
pie_data2 = [('SET TARGET',  939250000.00), ('ACHIEVED TARGET', progress2)]
# Specify colors for pie chart slices
colors = ['#00203FFF','#ADEFD1FF']  # green for SET TARGET, red for ACHIEVED TARGET

# Execute the query to fetch data for the scatter diagram-NPL
cursor.execute("select BookBal,AccountDesc from VwAccMaster  where CreditClassDesc !='performing' AND RelationshipOfficerName='OKAFOR, ERIC UCHENNA' and PostingDateAdded <='2023-12-31' order by PostingDateAdded asc")
scatter_data = cursor.fetchall()
  
mname_data = 'TEST,TEST'

# Create a dictionary to store the data for the charts
data = {
    'bar': [go.Bar(x=[row[0] for row in bar_data], y=[row[1] for row in bar_data],marker=dict(color='#000080'))],
    'pie': [go.Pie(labels=[row[0] for row in pie_data], values=[row[1] for row in pie_data],marker=dict(colors=colors))],
    'pbt': [go.Pie(labels=[row[0] for row in pbt_data], values=[row[1] for row in pbt_data],marker=dict(colors=colors))],
    'soh': [go.Pie(labels=[row[0] for row in soh_data], values=[row[1] for row in soh_data],marker=dict(colors=colors))],
    'pie2':[go.Pie(labels=[row[0] for row in pie_data2], values=[row[1] for row in pie_data2],marker=dict(colors=colors))],
    'bar2':[go.Bar(x=[row[0] for row in scatter_data], y=[row[1] for row in scatter_data],marker=dict(color='#000080'))],
}


# Create a dictionary to store the data for cards visualisation
values = {
    'RelationshipOfficerName': mname_data,
    
}

# Create a dictionary to store the data for cards visualisation
app.layout = html.Div( style={'backgroundColor': '#C0C0C0','height': 'auto','padding-top': '15px'},children=[
    html.H4(children='INFINITY TRUST MORTGAGE BANK',style={'color':'#00203FFF','text-align':'center','bgcolor':'#85c1e9'}),
    html.H4(children='My Marketer Dashboard',style={'color':'#00203FFF','text-align':'center'}),
    html.H4(children=f'{values["RelationshipOfficerName"]}  ',style={'color':'#00203FFF','text-align':'center'}),
    html.Div(children=[   
	html.H5(children=f'SUMMARY OF PERFORMANCE BY MARKETER',style={'color':'#00203FFF','text-align':'center','background':'ash'})
	
    ]
    ), 
   
       
       dcc.Tabs(id='tabs', value='NPL',style={'backgroundColor': '#85c1e9'},  children=[
       dcc.Tab(label='NPL ', value='NPL',style={'backgroundColor': '#85c1e9','color':'#00203FFF'}, children=[
       
            dcc.Graph(
                id='bar-chart',
                figure={
                    'data': data['bar2'],
                    'layout': {
                        'title': '',
                        'paper_bgcolor':'#C0C0C0',
                        'plot_bgcolor':'#C0C0C0',
                        'font':{
                            'color':'white'
                    }
                    }
                })
        ]),
        
    dcc.Tab(label='Target(Deposits)', value='Pie2',style={'backgroundColor': '#85c1e9','color':'#00203FFF'}, children=[
            dcc.Graph(
                id='pie-chart',
                figure={
                    'data': data['pie2'],
                    'layout': {
                        'title': '',
                        'paper_bgcolor':' #C0C0C0 ',
                        'plot_bgcolor':'',
                        'font':{
                            'color':'white'
                    }
                    }
                })
        ]),
       dcc.Tab(label='PBT', value='pbt',style={'backgroundColor': '#85c1e9','color':'#00203FFF'}, children=[
            dcc.Graph(
                id='pie-chart',
                figure={
                    'data': data['pbt'],
                    'layout': {
                        'title': '',
                         'paper_bgcolor':'#C0C0C0',
                        'plot_bgcolor':'',
                        'font':{
                            'color':'white'
                    }
                    }
                 })
        ]),
       
    dcc.Tab(label='Market Stop', value='soh',style={'backgroundColor': '#85c1e9','color':'#00203FFF'}, children=[
            dcc.Graph(
                id='pie-chart',
                figure={
                    'data': data['soh'],
                    'layout': {
                        'title': '',
                        'paper_bgcolor':'#C0C0C0',
                        'plot_bgcolor':'',
                        'font':{
                            'color':'white'
                    }
                    }
                })
        ]),
       
     dcc.Tab(label='Loans ', value='Bar chart',style={'backgroundColor': '#85c1e9','color':'#00203FFF'}, children=[
            dcc.Graph(
                id='bar-chart',
                figure={
                    'data': data['bar'],
                    'layout': {
                        'title': '',
                        'paper_bgcolor':'#C0C0C0',
                        'plot_bgcolor':'#C0C0C0',
                        'font':{
                            'color':'white'
                    }
                    }
                })
        ]),
        dcc.Tab(label='Target(Loans)', value='Pie',style={'backgroundColor': '#85c1e9','color':'#00203FFF'}, children=[
            dcc.Graph(
                id='pie-chart',
                figure={
                    'data': data['pie'],
                    'layout': {
                        'title': '',
                        'paper_bgcolor':'#C0C0C0 ',
                        'plot_bgcolor':'black',
                        'font':{
                            'color':'white'
                    }
                    }
                        })
                ])
            ]),

        # Footer section
        html.Footer(
            children=[
                html.Div(
                    children=[
                        html.P("ALL RIGHTS RESERVED.POWERED BY INFINITY TRUST MORTGAGE BANK PLC-2023",style={'color':'#00203FFF','text-align':'center','backgroundColor': '#C0C0C0','height': '70px'})
                    ],
                    className="footer-content"
                )
            ],
            className="footer"
        )
    ]
    
   
)
if __name__ == '__main__':
    app.run_server(debug='true',host='10.2.2.50', port=8001)












