import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import pytesseract
from PIL import Image
import re

response = requests.get("http://127.0.0.1:8000/get-taken-id")
id_list = response.json()

@st.cache
def get_total(selected_id):
    response = requests.get(f"http://127.0.0.1:8000/get-total-by-id/{selected_id}")
    return response.json()

st.title("Industry Project! 🏭")

st.header("📅 Week-1")

st.subheader("""
TOTAL prediction Web App
""")

st.write("This app predicts the total for a given invoice using Streamlit and by integrating API created using FastAPI")

selected_id = st.selectbox('Select unique invoice ID', id_list)
st.write(f"TOTAL predicted:")
st.write(get_total(selected_id))

st.header("OR...")
path = st.text_input("Enter path", value = "invoice-template-us-neat-750px.png")
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = str(((pytesseract.image_to_string(Image.open(f"{path}")))))
text = text.replace(',', '')
lst = re.findall('[-+]?([0-9]+\.[0-9]*)[^%]', text)
lst = np.array([float(i) for i in lst])
st.write(lst.max())

expander_bar = st.expander("About")
expander_bar.write("""
**Python libraries:** FastAPI, numpy, pandas, Pillow, PyTesseract, Streamlit

**Credit:** App built by Krishna Shetty
""")

