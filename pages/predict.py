import pickle
import pandas as pd
import streamlit as st

def app():
    st.header("Will it Rain tomorrow?")
    st.header("Select the values of all of the features given below, these values must correspond to the present day.")
    st.markdown('---')
    col1, col2, col3 = st.columns(3)

    with col1:
        rainfall = st.slider('Amount of Rainfall (mm)',
        min_value = 0.0, max_value = 20.0, value = 10.0)
        st.markdown('###')

        gust_speed = st.slider( 'Amount of Gust speed (km/h)',
        min_value = 0.0, max_value = 50.0, value = 25.0)
        st.markdown('###')

        avg_cloud = st.slider( 'Amount of Cloud coverage (oktas)',
        min_value = 0.0, max_value = 10.0, value = 5.0)
        st.markdown('###')

    with col2:
        evaporation = st.slider('Amount of Evaporation (mm)',
        min_value = 0.0, max_value = 20.0, value = 10.0)
        st.markdown('###')

        wind_speed = st.slider('Amount of Wind speed (km/h)',
        min_value = 0.0, max_value = 60.0, value = 30.0)
        st.markdown('###')

        avg_pressure = st.slider('Amount of Pressure (hpa)',
        min_value = 950.0, max_value = 1050.0, value = 1000.0)
        st.markdown('###')

    with col3:
        sunshine = st.slider('Amount of Sunshine (hours)',
        min_value = 0.0, max_value = 20.0, value = 10.0)
        st.markdown('###')

        humidity = st.slider('Amount of Humidity (%)',
        min_value = 0.0, max_value = 90.0, value = 45.0)
        st.markdown('###')
        temp_diff = st.slider('Amount of Temp. difference (°C)',
        min_value = -15.0, max_value = 35.0, value = 10.0)
        st.markdown('###')
    st.markdown('---')
    c1, c2 = st.columns(2)

    with c1:
        gust_dir = st.select_slider('Select Gust direction', options=[
            'W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW', 'ENE',
        'SSE', 'S', 'NW', 'SE', 'ESE', 'E', 'SSW'
        ])
        st.markdown('###')

        wind_dir = st.select_slider('Select Wind direction', options=[
            'W', 'NNW', 'SE', 'ENE', 'SW', 'SSE', 'S', 'NE', 'SSW', 'N',
        'WSW', 'ESE', 'E', 'NW', 'WNW', 'NNE'
        ])
    with c2:
        rain_today = st.selectbox('Did it Rain today?', ('Yes', 'No'))
        st.markdown('###')

        location = st.selectbox('Select Location', (
            'Adelaide',
            'Albany',
            'Albury',
            'AliceSprings',
            'BadgerysCreek',
            'Ballarat',
            'Bendigo',
            'Brisbane',
            'Cairns',
            'Canberra',
            'Cobar',
            'CoffsHarbour',
            'Dartmoor',
            'Darwin',
            'GoldCoast',
            'Hobart',
            'Katherine',
            'Launceston',
            'Melbourne',
            'MelbourneAirport',
            'Mildura',
            'Moree',
            'MountGambier',
            'MountGinini',
            'Newcastle',
            'Nhil',
            'NorahHead',
            'NorfolkIsland',
            'Nuriootpa',
            'PearceRAAF',
            'Penrith',
            'Perth',
            'PerthAirport',
            'Portland',
            'Richmond',
            'Sale',
            'SalmonGums',
            'Sydney',
            'SydneyAirport',
            'Townsville',
            'Tuggeranong',
            'Uluru',
            'WaggaWagga',
            'Walpole',
            'Watsonia',
            'Williamtown',
            'Witchcliffe',
            'Wollongong',
            'Woomera',
        ))

    st.markdown('---')
    final_list = [location, rainfall, evaporation, sunshine, gust_dir, gust_speed,
    wind_dir, wind_speed, humidity, avg_cloud, rain_today, avg_pressure, temp_diff]
    st.write(final_list)

    final_pred_df = pd.DataFrame([final_list], columns=['Location', 'Rainfall', 'Evaporation',
    'Sunshine', 'WindGustDir', 'WindGustSpeed', 'AvgWindDir', 'AvgWindSpeed', 'AvgHumidity',
    'AvgCloud', 'RainToday', 'AvgPressure', 'TempDiff'])

    # with open("pickles/final_model.sav", "rb") as file_model:
    #     final_model = pickle.load(file_model)

    # with open("pickles/full_pipeline.sav", "rb") as file_pipeline:
    #     full_pipeline = pickle.load(file_pipeline)

    # final_prep_df = full_pipeline.transform(final_pred_df)
    # # st.write(final_prep_df)
    # final_result = final_model.predict(final_prep_df)
    # st.write(final_result)