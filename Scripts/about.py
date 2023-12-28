import dash
from dash import html

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
            className="about",
            style={'text-align': 'center'},
            children=[
                html.H2("About"),
                html.P(
                    "Marketers Dasboard is a cutting-edge marketer dashboard app designed to empower businesses with comprehensive insights into the performance of their marketing teams. With a focus on key indicators such as Net Promoter Score (NPS), market stock, profit before tax (PBT), loans, and deposits, our app provides a holistic view of your marketing strategies and their impact on your company's growth."
                    "Moreover, the app goes beyond surface-level metrics by providing insights into financial performance. By analyzing PBT, loans, and deposits, you can assess the monetary impact of your marketing initiatives, aligning your strategies with business objectives and ensuring profitability."
                ),
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
    app.run_server(debug=True,host='10.1.0.119', port=9010)
