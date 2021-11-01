import streamlit as st
from PIL import Image
import pandas as pd
import requests 
import json 
from io import BytesIO

response = requests.get('https://i.pinimg.com/564x/6d/3c/5f/6d3c5f0eeaa113dbe97128e26a079733.jpg')
logo = Image.open(BytesIO(response.content))
st.image(logo, width=400)
st.title('Currency Converter App')
st.markdown("""
This app interconverts a given amount from ```Euro``` to any foreign currency!
""")

st.sidebar.header('Input Options')

currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

symbols_price_unit = st.sidebar.selectbox('Select target currency to convert to from Euro', currency_list)
amount = st.number_input(label="What amount you want to convert?",step=1.,format="%.2f")

@st.cache
def load_data():
    url = ''.join(['http://api.exchangeratesapi.io/v1/latest?access_key=7881f4528b452f8a9434b3310f4d719b&symbols=', symbols_price_unit])
    response = requests.get(url)
    data = response.json()
    base_currency = pd.Series( data['base'], name='base_currency')
    rates_df = pd.DataFrame.from_dict( data['rates'].items() )
    rates_df.columns = ['converted_currency', 'price']
    rates_df['price']=rates_df['price']*amount
    conversion_date = pd.Series( data['date'], name='date' )
    df = pd.concat( [base_currency, rates_df, conversion_date], axis=1 )
    return df

df = load_data()

st.header('Currency conversion')

st.write(df)