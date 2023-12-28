import dash
import pyodbc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundColor': '#C0C0C0',
        'height': 'auto',
        'padding-top': '15px',
        'align': 'center'
    },
    children=[
        html.Div(
            className="menu",
            children=[
                html.Ul(
                    style={'text-align': 'center', 'text-decoration': 'none'},
                    children=[
                        html.H4(children='INFINITY TRUST MORTGAGE BANK', style={'color': '#00203FFF', 'text-align': 'center', 'bgcolor': '#85c1e9'}),
                        html.H4(children=' Marketers Dashboard', style={'color': '#00203FFF', 'text-align': 'center'}),
                        html.A("HOME  |", href="http://10.1.0.119:9009/", style={'text-align': 'center', 'text-decoration': 'none'}),
                        html.A("DASHBOARD  |", href="http://10.1.0.119:9008/", style={'text-align': 'center', 'text-decoration': 'none'}),
                        html.A("ABOUT  |", href="http://10.1.0.119:9010/", style={'text-align': 'center', 'text-decoration': 'none'}),
                    ]
                )
            ],
        ),
        html.Div(
            className="links",
            style={'text-align': 'center'},
            children=[
                html.A("HEAD OFFICE BRANCH", href="http://10.1.0.119:9000/", style={'font-weight': 'bold', 'margin': '10px'}),
                html.A("HEAD OFFICE SBU 1", href="http://10.1.0.119:9005/", style={'font-weight': 'bold', 'margin': '10px'}),
                html.A("HEAD OFFICE SBU 2", href="http://10.1.0.119:9006/", style={'font-weight': 'bold', 'margin': '10px'}),
                html.A("MARARABA BRANCH", href="http://10.1.0.119:9004/", style={'font-weight': 'bold', 'margin': '10px'}),
                html.A("SUNCITY BRANCH", href="http://10.1.0.119:9007/", style={'font-weight': 'bold', 'margin': '10px'}),
                html.A("ILUPEJU BRANCH", href="http://10.1.0.119:9001/", style={'font-weight': 'bold', 'margin': '10px'}),
                html.A("ILUPEJU SBU ", href="http://10.1.0.119:9002/", style={'font-weight': 'bold', 'margin': '10px'}),
                html.A("KADUNA", href="http://10.1.0.119:9003/", style={'font-weight': 'bold', 'margin': '10px'}),
                
            ],
        ),
        html.Div(
            className="footer",
            children=[
                html.P("ALL RIGHTS RESERVED.POWERED BY INFINITY TRUST MORTGAGE BANK PLC-2023",
                       style={'color': '#00203FFF', 'text-align': 'center', 'backgroundColor': '#C0C0C0',
                              'height': '70px'}),
            ],
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True,host='10.1.0.119', port=9008)
