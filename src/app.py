    # Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data/data.csv')

fig = px.line(df, x="date", y="sales", title="Sales over the years")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Soul Foods',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Br(),
    html.Label('Radio Items'),
    dcc.RadioItems(df['region'].unique(), id='radio-items', style={'padding': 10, 'flex': 1, 'color': colors['text']
    }),

    dcc.Graph(
        id='line-plot',
        figure=fig
    )
])

@callback(
    Output('line-plot', 'figure'),
    Input('radio-items', 'value'))
def update_figure(region):
    filtered_df = df[df['region'] == region]

    fig = px.line(filtered_df, x="date", y="sales", title="Sales over the years")

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run(debug=True)

