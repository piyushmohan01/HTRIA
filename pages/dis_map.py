import datetime
import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
# from sklearn.preprocessing import StandardScaler
def app():
    st.header('HTRIA')

    weather_data = pd.read_csv('data/weather_data.csv')
    weather_data = weather_data.loc[:, 'Location':]
    st.write(weather_data['TempDiff'].describe())

    inp_date = st.date_input('', datetime.date(2010, 1, 1))
    inp_day = inp_date.day
    inp_month = inp_date.month
    inp_year = inp_date.year

    sub_data = weather_data.loc[(weather_data['Day'] == inp_day) & (weather_data['Month'] == inp_month) & (weather_data['Year'] == inp_year)]
    st.write(sub_data)

    # scaler = StandardScaler()
    # sub_data['Rainfall'] = sub_data['Rainfall'].apply(StandardScaler())

    # num_cols = sub_data.select_dtypes(np.number).columns.tolist()
    # sub_data[num_cols] /= sub_data[num_cols].max()

    m = folium.Map(
        location=[-28.020267, 133.769519], 
        tiles='Stamen Watercolor', zoom_start=4,
    )

    folium.Circle(
        location=[-24.56267, 133.769519],
        radius=100000, color='red', fill=True,
        popup='Some-Text',
    ).add_to(m)

    def rainfall_circles(x):
        folium.CircleMarker(
            location=[x[0], x[1]],
            radius=float(x[3]),
            color='red', fill=True,
            popup='Location : {}'.format(x[2])
        ).add_to(m)

    def evaporation_circles(x):
        folium.CircleMarker(
            location=[x[0], x[1]],
            radius=float(x[3]),
            color='yellow', fill=True,
            popup='Location : {}'.format(x[2])
        ).add_to(m)

    def sunshine_circles(x):
        folium.CircleMarker(
            location=[x[0], x[1]],
            radius=float(x[3]),
            color='blue', fill=True,
            popup='Location : {}'.format(x[2])
        ).add_to(m)

    sub_data[['Latitude', 'Longitude', 'Location', 'Rainfall']].apply(lambda x: rainfall_circles(x), axis=1)
    # sub_data[['Latitude', 'Longitude', 'Location', 'Evaporation']].apply(lambda x: evaporation_circles(x), axis=1)
    # sub_data[['Latitude', 'Longitude', 'Location', 'Sunshine']].apply(lambda x: sunshine_circles(x), axis=1)

    folium_static(m)