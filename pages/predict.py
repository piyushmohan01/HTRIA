import pickle
import pandas as pd
import streamlit as st

def app():
    st.subheader("Will it Rain tomorrow? Enter today's values and find out!")
    st.markdown('---')

    # --- Splitting into 3 Columns ---
    col1, col2, col3 = st.columns(3)

    # --- Column 1 ---
    with col1:
        rainfall = st.slider('Amount of Rainfall (mm)',
        min_value = 0.0, max_value = 20.0, value = 15.6)
        st.markdown('###')

        gust_speed = st.slider( 'Amount of Gust speed (km/h)',
        min_value = 0.0, max_value = 80.0, value = 61.0)
        st.markdown('###')

        avg_cloud = st.slider( 'Amount of Cloud coverage (oktas)',
        min_value = 0.0, max_value = 10.0, value = 8.0)
        st.markdown('###')

    # --- Column 2 ---
    with col2:
        evaporation = st.slider('Amount of Evaporation (mm)',
        min_value = 0.0, max_value = 20.0, value = 4.8)
        st.markdown('###')

        wind_speed = st.slider('Amount of Wind speed (km/h)',
        min_value = 0.0, max_value = 60.0, value = 28.0)
        st.markdown('###')

        avg_pressure = st.slider('Amount of Pressure (hpa)',
        min_value = 950.0, max_value = 1050.0, value = 993.0)
        st.markdown('###')

    # --- Column 3 ---
    with col3:
        sunshine = st.slider('Amount of Sunshine (hours)',
        min_value = 0.0, max_value = 20.0, value = 8.5)
        st.markdown('###')

        humidity = st.slider('Amount of Humidity (%)',
        min_value = 0.0, max_value = 120.0, value = 93.0)
        st.markdown('###')

        temp_diff = st.slider('Amount of Temp. difference (°C)',
        min_value = -15.0, max_value = 35.0, value = 2.70)
        st.markdown('###')
    
    st.markdown('---')

    # --- Splitting into 2 Columns ---
    c1, c2 = st.columns(2)

    # --- Column 1 ---
    with c1:
        gust_dir = st.select_slider('Select Gust direction', options=[
            'W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW', 'ENE',
        'SSE', 'S', 'NW', 'SE', 'ESE', 'E', 'SSW'
        ])
        st.markdown('###')

        wind_dir = st.select_slider('Select Wind direction', options=[
            'NNW', 'W', 'SE', 'ENE', 'SW', 'SSE', 'S', 'NE', 'SSW', 'N',
        'WSW', 'ESE', 'E', 'NW', 'WNW', 'NNE'
        ])

    # --- Column 2 ---
    with c2:
        rain_today = st.selectbox('Did it Rain today?', ('Yes', 'No'))
        st.markdown('###')

        location = st.selectbox('Select Location', (
            'Albury',
            'Adelaide',
            'Albany',
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

    # --- Final list of Input values ---
    final_list = [location, rainfall, evaporation, sunshine, gust_dir, gust_speed,
    wind_dir, wind_speed, humidity, avg_cloud, rain_today, avg_pressure, temp_diff]

    starter_list = ['Albury', 15.6000, 4.8000, 8.5000, 'W', 61.0000, 'NNW',
    28.0000, 93.0000, 8.0000, 'Yes', 993.0000, 2.7000]

    # --- Creating Single-Row DataFrame ---
    final_pred_df = pd.DataFrame([final_list], columns=['Location', 'Rainfall', 'Evaporation',
    'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir3pm', 'AvgWindSpeed', 'Humidity3pm',
    'Cloud3pm', 'RainToday', 'Pressure3pm', 'TempDiff'])
    st.write(final_pred_df)
    st.markdown("---")

    # --- Opening the Pickle files ---
    with (open("pickles/final_model.sav", "rb")) as file_model:
            final_model = pickle.load(file_model)

    with (open("pickles/full_pipeline.sav", "rb")) as file_pipeline:
            full_pipeline = pickle.load(file_pipeline)
    
    # --- Preparing DataFrame for prediction ---
    final_prep_df = full_pipeline.transform(final_pred_df)

    # --- Predicting with prepared DataFrame ---
    final_result = final_model.predict(final_prep_df)
    if final_result == 'Yes':
        if final_list == starter_list:
            st.info('The default values were set to give "Yes" as the outcome! Try changing the values above!')
        else: 
            st.info('Yes! You definitely will see some rain tomorrow!')
    else:
        st.info('No! You won\'t be seeing any rain tomorrow!')
