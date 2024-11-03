import tensorflow as tf
import pandas as pd
import numpy as np
import keras
import argparse
import sys
from datetime import datetime
from utils import json_to_dataframe, drop_columns, feature_engineer, normalise, get_drop_identifiers, feature_selection

def load_data(data):
    try:
        df = json_to_dataframe(data)
        df1 = drop_columns(df)
        df2 = feature_engineer(df1)
        df3 = normalise(df2)
        df4 = normalise(df3)
        identifiers, df5 = get_drop_identifiers(df4)
        df6 = feature_selection(df5)

        # Reshape data for CNN compatibility
        data_reshaped = np.expand_dims(df6.values, axis=2)

        return identifiers, data_reshaped
    except Exception as e:
        print(f"Error loading or preparing data: {e}")
        sys.exit(1)

def load_model(model_path):
    try:
        model = keras.models.load_model(model_path)
        print(model.summary())
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

def main(model_path, data_path, n, output_filename):
    model = load_model(model_path)
    identifiers, data_reshaped = load_data(data_path)
    
    # Make predictions
    predictions = model.predict(data_reshaped)
    
    # Create predictions dataframe with identifiers
    identifiers['score'] = predictions
    
    # Save predictions
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

     # If no specific file name is provided, use the default format
    if output_filename is None:
        final_filename = f"output/model_output_{formatted_datetime}.csv"
    else:
        final_filename = f"output/{output_filename}.csv"

    identifiers.to_csv(final_filename, index=False)

    print("Predictions with identifiers:")
    print(identifiers.head(n))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run CNN model on test data to get m6a modification probabilities")
    parser.add_argument("--model_path", type=str, default="cnn_selected.h5", help="Path to the trained model file")
    parser.add_argument("--data_path", type=str, default="data/test_data.json", help="Path to the test dataset with identifiers")
    parser.add_argument("--n", type=int, default=10, help="Number of rows of predictions to print in console")
    parser.add_argument("--output_filename", type=str, help="File name of the model predictions output")
    args = parser.parse_args()

    main(args.model_path, args.data_path, args.n, args.output_filename)
