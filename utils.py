## Importing required libraries
import pandas as pd
from pycaret.datasets import get_data
from pycaret.clustering import *
from yaml import CLoader as Loader, load

## Function for reading config file
def read_config(path):
    with open(path) as stream:
        config = load(stream,Loader=Loader)
    return config

## Function to get data
def get_dataset(dataset_name):
    jewel_data = get_data(dataset_name)
    return jewel_data

## Function to return the shape of data
def get_data_shape(data):
    print("\nThe shape of the data is ",data.shape)

# Function to save predictions as a csv file
def save_predictions(predictions, output_path, **kwargs):
    output_path += "/test.csv"
    predictions.to_csv(output_path,index=False)