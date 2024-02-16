import streamlit as st
import requests
import plotly.graph_objects as go

api_key = 'd711e292439bac5ac4a771bbe3a4c704'
st.markdown("<h1 style='text-align: center;'>Weather Dashboard</h1>", unsafe_allow_html=True)
location_input = st.text_input("", "Bloomsburg", key="location_input")

if location_input:
    if location_input.isdigit():
        params = {'zip': location_input, 'appid': api_key}
    else:
        params = {'q': location_input, 'appid': api_key}

    api_endpoint = 'https://api.openweathermap.org/data/2.5/weather?units=imperial'

    response = requests.get(api_endpoint, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        
        st.write(f"Temperature: {data['main']['temp']}°F &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Humidity: {data['main']['humidity']}% &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Wind Speed: {data['wind']['speed']} m/s")
        fig1 = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=data['wind']['deg'],
            mode="gauge+number",
            title={'text': "Wind degree"},
            gauge={'axis': {'range': [None, 50]},
                   'bar': {'color': "darkblue"},
                   'steps': [
                       {'range': [0, 15], 'color': "cyan"},
                       {'range': [15, 30], 'color': "royalblue"},
                       {'range': [30, 50], 'color': "darkblue"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 30}}))

        

        fig2 = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=data['main']['pressure'],
            mode="gauge+number",
            title={'text': "Pressure"},
            gauge={'axis': {'range': [None, 1100]},
                   'bar': {'color': "darkgreen"},
                   'steps': [
                       {'range': [0, 500], 'color': "lightgreen"},
                       {'range': [500, 900], 'color': "green"},
                       {'range': [900, 1100], 'color': "darkgreen"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 1000}}))
        
        labels = ['Wind Gust', 'Wind Speed', 'Wind Degree']
        values = [2, 2, 15]  

        fig_donut = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

        fig_donut.update_layout(title='other Information',
                                annotations=[dict(text='Total', x=0.5, y=0.5, font_size=20, showarrow=False)])

        st.plotly_chart(fig_donut)

        col1, col2 = st.columns(2)

with col1:
    st.write('<style>div.Widget.row-widget.stRadio div[role="radiogroup"] > label {text-align: right;} </style>', unsafe_allow_html=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.write('<style>div.Widget.row-widget.stRadio div[role="radiogroup"] > label {text-align: left;} </style>', unsafe_allow_html=True)
    st.plotly_chart(fig2, use_container_width=True)


