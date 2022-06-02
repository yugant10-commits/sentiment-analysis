import typing
from ast import Str

import plotly.express as px
import streamlit as st


@st.cache(allow_output_mutation=True)
def make_radar_graph(dict: typing.Dict[Str, float]):
    fig = px.line_polar(
        r=dict.values(),
        theta=dict.keys(),
        line_close=True,
        template="plotly_dark",
        direction="counterclockwise",
        color_discrete_sequence=px.colors.sequential.Plasma_r,
    )
    return fig
