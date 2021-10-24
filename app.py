import streamlit as st
from multiapp import MultiApp
from pages import map_viz, predict

st.title("How's the rain in Australia?")

# --- Initializing MultiApp ---
app = MultiApp()

# --- Adding apps to MultiApp ---
app.add_app("Prediction Page", predict.app)
app.add_app("Map Visualizations", map_viz.app)

# --- Running Main app ---
app.run()

st.sidebar.markdown("Project by Team 404 for HTF-2.0")
st.sidebar.markdown("[Find more about the project on Github](https://github.com/piyushmohan01/HTRIA)")
