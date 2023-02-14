## Importing required libraries
from pycaret.clustering import *
import pickle

## Building kmeans clustering model
def build_model(model_name, no_of_clusters):
    kmeans = create_model('kmeans',4)
    return kmeans

## Assigning the cluster labels to our dataset
def assign_cluster_model(model_var_name):
    kmean_results = assign_model(model_var_name)
    return kmean_results

# Function to save model
def save_final_model(model,model_path):
    model_path += '/Final_kmeans_model'
    save_model(model,model_path)




## Function to load model
def load_presaved_model(model_path):
    model_path += '/Final_kmeans_model'
    return load_model(model_path)

