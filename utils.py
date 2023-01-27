import pickle
import pandas as pd

car_df = pd.read_csv("cars.csv")

filename = "ideal_model.pkl"

loaded_model = pickle.load(open(filename, "rb"))

def preprocess_data(input_data):
  """
  This function takes the input data dictionary as argument, 
  converts string data type and returns the dataframe. 
  """
  input_df = pd.DataFrame(data=input_data, index=[0])

  for label, content in input_df.items():
    if pd.api.types.is_string_dtype(content):
      input_df[label] = content.astype("category").cat.codes

  return input_df


def predict_price(processed_data):
  """
  This function predicts the price based on the processed data
  """
  result = round(loaded_model.predict(processed_data)[0], 0)
  return result





