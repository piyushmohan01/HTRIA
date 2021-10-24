import datetime
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static

@st.cache()
def load_data():
    weather_data = pd.read_csv('data/weather_data.csv')
    weather_data = weather_data.loc[:, 'Location':]
    return weather_data

def app():

    st.subheader('Get day-wise insights for all the numerical features!')

    # --- Load Dataset ---
    weather_data = load_data()

    # --- Date Picker for Input Date ---
    inp_date = st.date_input('Select your Date', datetime.date(2016, 1, 1))
    inp_day = inp_date.day
    inp_month = inp_date.month
    inp_year = inp_date.year

    # --- Slicing DataFrame with Input Date ---
    sub_data = weather_data.loc[(weather_data['Day'] == inp_day) & (weather_data['Month'] == inp_month) & (weather_data['Year'] == inp_year)]

    # --- Letting the user pick Map styles ---
    tile_options = ['Stamen Toner', 'Stamen Terrain', 'Stamen Watercolor', 'OpenStreetMap']
    tile_type = st.selectbox(label='Select Map type',
    options=(
        'Stamen Toner', 'Stamen Terrain', 'Stamen Watercolor', 'OpenStreetMap'
    ))

    # --- Defining Folium Map object ---
    m = folium.Map(
        location=[-28.020267, 133.769519], 
        tiles=tile_type, zoom_start=4,
    )

    # --- Placing Marker for reference ---
    folium.Marker(
        location=[-24.56267, 133.769519],
        popup='Australia',
    ).add_to(m)

    # --- Function to populate map with markers ---
    def feature_circles(feature, x, color):
        if feature == 'AvgPressure':
            feature_radius = float(x[3]/50)
        elif feature == 'AvgHumidity':
            feature_radius = float(x[3]/5)
        else:
            feature_radius = float(x[3])
        folium.CircleMarker(
            location=[x[0], x[1]],
            radius=feature_radius,
            color=color, fill=True,
            popup='Location: {}\n{}: {}'.format(x[2], feature, x[3])
        ).add_to(m)

    # --- Feaute-Color Dictionary ---
    num_features = {
        'Rainfall':'darkblue',
        'Evaporation':'red',
        'Sunshine':'orange',
        'WindGustSpeed':'pink',
        'AvgWindSpeed':'beige',
        'AvgHumidity':'purple',
        'AvgCloud':'green',
        'AvgPressure':'darkgreen',
        'TempDiff':'gray',
    }

    # --- Letting the user pick features ---
    selected_features = st.multiselect(label='Select your features',
    options=(
        'Rainfall', 'Evaporation', 'Sunshine',
        'WindGustSpeed', 'AvgWindSpeed', 'AvgHumidity',
        'AvgCloud', 'AvgPressure', 'TempDiff',
    ))

    # --- Calling feature_circles(...) ---
    for feature, color in num_features.items():
        if feature in selected_features:
            sub_data[[
                'Latitude', 'Longitude', 'Location', feature
            ]].apply(lambda x: feature_circles(
                feature, x, color), axis=1)

    # --- Rendering Map in Streamlit ---
    folium_static(m)
    
    # --- Option to view Raw-Data based on Date ---
    view_data = st.checkbox(label='View Data for your date', value=False)
    if view_data: st.write(sub_data)
