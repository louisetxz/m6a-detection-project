import tensorflow as tf
import pandas as pd
import numpy as np
import argparse
import sys
from datetime import datetime

def load_model(model_path):
    try:
        model = tf.keras.models.load_model(model_path)
        print(model.summary())
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

def load_data(data_path):
    try:
        data = pd.read_csv(data_path)
        print("Data preview:")
        print(data.head())
        
        # Extract identifiers
        identifiers = data[['transcript_id', 'transcript_position']]
        
        # Drop identifier columns for model input
        new_data = data.drop(columns=['transcript_id', 'transcript_position'], errors='ignore')
        
        # Reshape data for CNN compatibility
        data_reshaped = np.expand_dims(new_data.values, axis=2)
        
        return identifiers, data_reshaped
    except Exception as e:
        print(f"Error loading or preparing data: {e}")
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
    parser.add_argument("--model_path", type=str, default="cnn_selected.keras", help="Path to the trained model file")
    parser.add_argument("--data_path", type=str, default="/data/test_data.csv", help="Path to the test dataset with identifiers")
    parser.add_argument("--n", type=int, default=10, help="Number of rows of predictions to print in console")
    parser.add_argument("--output_filename", type=str, help="File name of the model predictions output")
    args = parser.parse_args()

    main(args.model_path, args.data_path, args.n, args.output_filename)