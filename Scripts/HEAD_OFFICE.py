import dash
import pyodbc
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.graph_objs as go

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
# Connect to the SQL Server database

server = 'TEST-DBASE1'
database = 'EazybankAX1'
username = 'BIUser'
password = '1stepahead#'

# Create the connection string
connection_string = (
    f'DRIVER={{ODBC Driver 13 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

# Connect to the SQL Server database using the specified login credentials
cnxn = pyodbc.connect(connection_string)
# Create a cursor to execute queries
cursor = cnxn.cursor()

# Execute the query to fetch data for the bar chart-LOANS
cursor.execute("select a.AccountDesc as accountName,a.AmountGranted  as amountgranted from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.CreditTypeDesc='Mortgage Loan' and a.PostingDateAdded between '2023-01-01' and '2023-12-01' and RelationshipOfficerName in('JAIYESIMI, OLUWOLE ','Emmanuel, Sylvester ')")
bar_data = cursor.fetchall()

# Execute the query to fetch data for the pie chart-pbt
query ="select sum(a.AmountGranted)   from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.CreditTypeDesc='Mortgage Loan' and a.PostingDateAdded between '2023-01-01' and '2023-12-31' and RelationshipOfficerName in('JAIYESIMI, OLUWOLE ','Emmanuel, Sylvester')"
cursor = cnxn.cursor()
cursor.execute(query)
progress = cursor.fetchone()[0]
# update the `pie_data` list with the retrieved progress   
pbt_data = [('SET TARGET',    231511667), ('OUTSTANDING TARGET', progress)]
# Specify colors for pie chart slices
colors = ['#00203FFF','#ADEFD1FF']  # green for SET TARGET, red for ACHIEVED TARGET

# Execute the query to fetch data for the pie chart-sale of house
query ="select sum(a.AmountGranted)   from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.CreditTypeDesc='Mortgage Loan' and a.PostingDateAdded between '2023-01-01' and '2023-12-31' and RelationshipOfficerName in('JAIYESIMI, OLUWOLE ','Emmanuel, Sylvester')"
cursor = cnxn.cursor()
cursor.execute(query)
progress = cursor.fetchone()[0]
# update the `pie_data` list with the retrieved progress   
soh_data = [('SET TARGET',    57091667), ('OUTSTANDING TARGET', progress)]
# Specify colors for pie chart slices
colors = ['#00203FFF','#ADEFD1FF']  # green for SET TARGET, red for ACHIEVED TARGET

# Execute the query to fetch data for the pie chart-target(loans)
query ="select sum(a.AmountGranted)   from VwCreditMaster a,VwAccMaster b where a.AccountNo=b.AccountNo and a.CreditTypeDesc='Mortgage Loan' and a.PostingDateAdded between '2023-01-01' and '2023-12-31' and RelationshipOfficerName in('JAIYESIMI, OLUWOLE ','Emmanuel, Sylvester')"
cursor = cnxn.cursor()
cursor.execute(query)
progress = cursor.fetchone()[0]
# update the `pie_data` list with the retrieved progress   
pie_data = [('SET TARGET',   2040000000), ('OUTSTANDING TARGET', progress)]
# Specify colors for pie chart slices
colors = ['#00203FFF','#ADEFD1FF']  # green for SET TARGET, red for ACHIEVED TARGET

# Execute the query to fetch data for the pie chart2-target(deposits)
query2 ="select sum(a.BalAcctCurr) from VwTransHist a,VwAccMaster b where a.AccountNo=b.AccountNo and TransCode in('103','1031') and a.PostingDateAdded between '2023-01-01' and '2023-12-31' and  RelationshipOfficerName in('JAIYESIMI, OLUWOLE ','Emmanuel, Sylvester')"
cursor2 = cnxn.cursor()
cursor2.execute(query2)
progress2 = cursor2.fetchone()[0]
# update the `pie_data` list with the retrieved progress   
pie_data2 = [('SET TARGET',  2117323082), ('OUTSTANDING TARGET', progress2)]
# Specify colors for pie chart slices
colors = ['#00203FFF','#ADEFD1FF']  # green for SET TARGET, red for ACHIEVED TARGET

# Execute the query to fetch data for the scatter diagram-NPL
cursor.execute("select AccountDesc,BookBal from VwAccMaster  where CreditClassDesc !='performing' AND RelationshipOfficerName in('JAIYESIMI, OLUWOLE ','Emmanuel, Sylvester') and PostingDateAdded <='2023-12-31' order by PostingDateAdded asc")
scatter_data = cursor.fetchall()
  
mname_data = ''

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
sidebar = html.Div(
    [
        html.H6("HEAD OFFICE BRANCH", className="display-6"),
        html.Hr(),
        html.P("", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("NPL", href="/", active="exact"),
                dbc.NavLink("PBT", href="/pbt", active="exact"),
                dbc.NavLink("MARKET STOCK", href="/mst", active="exact"),
                dbc.NavLink("DEPOSITS(TARGET)", href="/tdpts", active="exact"),
                dbc.NavLink("LOANS", href="/loans", active="exact"),
                dbc.NavLink("LOANS(TARGET)", href="/tloans", active="exact"),
                dbc.NavLink("", href="", active="exact"),
                dbc.NavLink("BACK TO DASHBOARD", href="http://10.1.0.119:9008/", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
# Footer section
footer =html.Footer(
            children=[
                html.Div(
                    children=[
                        html.P("")
                    ],
                    className="footer-content"
                )
            ],
            className="footer"
        )

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content, footer])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        bar_chart = dcc.Graph(
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
        return html.Div(
            [
                html.H3("NPL"),
                html.Hr(),
                bar_chart,
            ]
        )
    elif pathname == "/pbt":
        pie_chart_1 = dcc.Graph(
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
        return html.Div(
            [
                html.H3("PBT"),
                html.Hr(),
                pie_chart_1,
            ]
        )
    elif pathname == "/mst":
        pie_chart_2 = dcc.Graph(
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
        return html.Div(
            [
                html.H3("MARKET STOCK"),
                html.Hr(),
                pie_chart_2,
            ]
        )
    elif pathname == "/tdpts":
        pie_chart_2 = dcc.Graph(
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
        
        return html.Div(
            [
                html.H3("DEPOSITS(TARGET)"),
                html.Hr(),
                pie_chart_2,
            ]
        )
    elif pathname == "/loans":
        pie_chart_2 = dcc.Graph(
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
        
        return html.Div(
            [
                html.H3("LOANS"),
                html.Hr(),
                pie_chart_2,
            ]
        )
        
    elif pathname == "/tloans":
        bar_chart_2 = dcc.Graph(
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
               
        return html.Div(
            [
                html.H3("LOANS(TARGET)"),
                html.Hr(),
                bar_chart_2,
            ]
        )
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognized..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(debug='true',host='10.1.0.119', port=9000)
