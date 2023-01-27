import streamlit as st
from utils import predict_price, preprocess_data

st.set_page_config(layout="wide")

st.title("Calculate the price of car")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
  brand = st.text_input(label="Brand")
  model = st.text_input(label="Model")
  kilometer = st.number_input(label="Kilometer run")
  year = st.number_input(label="Year")
  gearbox = st.radio(
    "Gearbox",
    ('Automatic', 'Manual', 'Front', 'AWD', 'Rear')
  )

with col2:
  fuel = st.radio(
    "Fuel",
    ('Unleaded Petrol', 'Diesel', 'Premium Unleaded Petrol',
      'Premium Unleaded/Electric', 'Unleaded Petrol/Electric',
      'Liquid Petroleum Gas', 'Diesel/Electric')
  )
  status = st.radio(
    "Status",
    ("Used", "New In Stock")
  )
  cc = st.number_input(label="CC")
  btn_clicked = st.button(
    label="Calculate", 
    key="calculateBtn"
  )

# create a dictionary of the data input by customer
input_data = {
  "brand": brand,
  "model": model,
  "kilometer": kilometer,
  "year": year,
  "gearbox": gearbox,
  "fuel": fuel,
  "status": status,
  "cc": cc
}

# get the processed data
processed_data = preprocess_data(input_data)

# call predict_price function after the submit button is clicked
if btn_clicked:
  result = predict_price(processed_data)
  st.write(f"Price: {result}")

