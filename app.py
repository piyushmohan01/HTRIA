# import pickle
# import pandas as pd
import streamlit as st
from multiapp import MultiApp
from pages import dis_map, predict

st.title("How's the rain in Australia?")

st.markdown('###')

app = MultiApp()

app.add_app("Predictions", predict.app)
app.add_app("Maps", dis_map.app )

app.run()