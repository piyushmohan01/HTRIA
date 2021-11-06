# HTRIA

- The unfortunate bushfires between 2019 and 2020 spiked some intrigue among people around the globe regarding the climatic situation in Australia. It brough attention to a topic that has been an annual discussion within the continent.

- Rain in Australia plays a bigger role than any other, it calms and eases the bushfires but also brings dangerous floods and storms with it. Yet, over the years, researchers and scientists have only found the level of percipitation to be decreasing with time. In fact, the overall average temperature of the continent has also increased during the period.

- With this project, we try to understand and work with the 'Rain in Australia' dataset and also try to provide a simple platform for users to interact and visualize various factors that affect the possibility of rain. Along with interactive and customizable maps, users can also try predicting a day after's rain by simply entering the present day's values.

- HTRIA, short for 'How's the Rain in Australia' is a project that explores and understands the rainfall patterns of **49 unique locations in Australia**. One can find details pertaining to any location on any distinct day and also get predictions on the chance of rain for the day after. Acknowledging the unpredictable weather conditions in the country, our model makes predictions by taking 15 features into account ([Kaggle Dataset](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package))

## Tech Stack :

    - Front-end :
        - Folium
        - Streamlit
        
    - Back-end :
        - Pickle
        - Scikit-Learn

## Try it out yourself :

- You can try out the app here : [HTRIA](https://share.streamlit.io/piyushmohan01/htria/app.py)
- Or run it yourself as shown below :

```
pip install -r requirements.txt
streamlit run app.py
```

- Our multipage Streamlit application consists of two pages :
    - **Predictions Page** : User enters the values of all the required features and the ML model predicts the chances of rain.\
    - **Maps Page** : User can get day-wise insights of all the numerical features visualized on the interactive map of Australia.

- If on the Predictions Page :
    - Try adjusting values with sliders and select-boxes
    - The predicted result will be displayed at the bottom
    - Navigate to the Visualizations page using the sidebar
- If on the Visualizations Page :
    - Pick a date from the data-picker by clicking on the datebox
    - Choose a Map Style from the select-box
    - Choose any feature(s) and watch the map get populated with markers
    - Move around the map using the pointer or zoom in and out

## What's next for HTRIA :

- [ ] Plots and Charts visualizing features with each other
- [ ] Improving the accuracy and ease of use for the users
