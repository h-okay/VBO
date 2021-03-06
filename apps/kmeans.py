import dash_bootstrap_components as dbc
from dash import html

from func import draw_kmeans, kmeans_table, segment_treemap

layout = dbc.Container(
    [
        html.H2(["TREE MAP"], id="clustering1"),
        html.Hr(),
        dbc.Row([dbc.Col([segment_treemap()])]),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H2(["HIERARCHICAL CLUSTERING"], id="clustering2"),
        html.Hr(),
        dbc.Row([dbc.Col([dbc.Card([kmeans_table()], id="table-card5")])]),
        dbc.Row(
            [
                dbc.Col([draw_kmeans()]),
            ]
        ),
    ]
)
