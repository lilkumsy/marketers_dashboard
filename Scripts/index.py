import dash
import pyodbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import flask
import os

app = dash.Dash(__name__)

# Define the list of image filenames
image_filenames = [
    "slide1.jpg",
    "slide2.jpg",
    "slide3.png",
]

image_directory = "C:/app/Scripts/img/"
image_urls = [f"/image/{filename}" for filename in image_filenames]

# Create a Flask server
server = app.server

# Serve the images
@server.route("/image/<filename>")
def serve_image(filename):
    image_path = os.path.join(image_directory, filename)
    if not os.path.exists(image_path):
        raise flask.abort(404)
    return flask.send_file(image_path, mimetype="image/jpeg")

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
            className="slideshow",
            children=[
                html.Img(id="slideshow-image", style={"width": "100%", 'height': '10%'}),
                dcc.Interval(id="slideshow-interval", interval=3000, n_intervals=0),
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

@app.callback(
    Output("slideshow-image", "src"),
    Input("slideshow-interval", "n_intervals"),
)
def update_slideshow_image(n):
    image_index = n % len(image_urls)
    return image_urls[image_index]

if __name__ == "__main__":
    app.run_server(debug=True,host='10.1.0.119', port=9009)
