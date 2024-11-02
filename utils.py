import pandas as pd
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def json_to_dataframe(json_file_path):
    data = []

    # Read the JSON file line by line
    with open(json_file_path, 'r') as file:
        for line in file:
            try:
                # Parse each line as a separate JSON object
                json_data = json.loads(line.strip())
                
                # Process `json_data` here as in your original code
                for transcript_id, positions in json_data.items():
                    for position, sequences in positions.items():
                        for sequence, reads in sequences.items():
                            fivemer_neg_1 = sequence[:5]
                            fivemer_0 = sequence[1:6]
                            fivemer_1 = sequence[2:]
                            
                            for read in reads:
                                row = [
                                    transcript_id,
                                    int(position)-1,
                                    read[0], read[1], read[2],
                                    int(position),
                                    read[3], read[4], read[5],
                                    int(position)+1,
                                    read[6], read[7], read[8],
                                    sequence,
                                    fivemer_neg_1,
                                    fivemer_0,
                                    fivemer_1
                                ]
                                data.append(row)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line}")
    
    columns = [
        'transcript_id', 'position_neg_1', 'dwelling_time_neg_1', 'sd_neg_1', 'mean_neg_1',
        'transcript_position', 'dwelling_time_0', 'sd_0', 'mean_0',
        'position_1', 'dwelling_time_1', 'sd_1', 'mean_1',
        'ori_nucleotide', 'fivemer_neg_1', 'fivemer_0', 'fivemer_1'
    ]
    
    df = pd.DataFrame(data, columns=columns)
    return df


def drop_columns(df):
    new_df = df.drop(columns=["ori_nucleotide","fivemer_neg_1","fivemer_0","fivemer_1"])
    return new_df

def feature_engineer(df):
    # Group by 'transcript_id' and 'gene_id' and calculate the mean for each column
    averaged_df = df.groupby(['transcript_id', 'transcript_position']).agg({
        'dwelling_time_neg_1': ['mean', 'min', 'max', 'median'],
        'dwelling_time_0': ['mean', 'min', 'max', 'median'],
        'dwelling_time_1': ['mean', 'min', 'max', 'median'],
        'mean_neg_1': ['mean', 'min', 'max', 'median'],
        'mean_0': ['mean', 'min', 'max', 'median'],
        'mean_1': ['mean', 'min', 'max', 'median'],
        'sd_neg_1': ['mean', 'min', 'max', 'median'],
        'sd_0': ['mean', 'min', 'max', 'median'],
        'sd_1': ['mean', 'min', 'max', 'median']
    }).reset_index()

    # Rename columns to desired format
    averaged_df.columns = [
        f'{col[0]}_{col[1]}' if col[1] != '' else col[0]  # Join column names with '_'
        for col in averaged_df.columns
    ]

    def add_rolling(df):
        # Define the pairs of columns to calculate differences for each metric
        calculations = {
            'dwelling_time': [('dwelling_time_neg_1_mean', 'dwelling_time_0_mean'), 
                            ('dwelling_time_0_mean', 'dwelling_time_1_mean')],
            'mean': [('mean_neg_1_mean', 'mean_0_mean'), 
                    ('mean_0_mean', 'mean_1_mean')],
            'sd': [('sd_neg_1_mean', 'sd_0_mean'), 
                ('sd_0_mean', 'sd_1_mean')]
        }

        for metric, pairs in calculations.items():
            for first, second in pairs:
                # Create a new column with a unique name for the difference
                df[f'{metric}_diff_{first}_{second}'] = df[first] - df[second]
        
        return df

    new_df = add_rolling(averaged_df)
    return new_df

def normalise(df):
    scaler = StandardScaler()

    excluded_columns = ['transcript_id', 'transcript_position']

    scaled_columns = [col for col in df.columns if col not in excluded_columns]

    df[scaled_columns] = scaler.fit_transform(df[scaled_columns])
    
    return df

def get_drop_identifiers(df):
    df1 = df.drop(columns=['transcript_id', 'transcript_position'])
    identifiers = df[['transcript_id', 'transcript_position']]
    return identifiers, df1

def feature_selection(df):
    top_features = ['sd_0_mean',
                    'mean_0_mean',
                    'mean_diff_mean_0_mean_mean_1_mean',
                    'sd_0_median',
                    'mean_0_median',
                    'mean_diff_mean_neg_1_mean_mean_0_mean',
                    'mean_1_mean',
                    'sd_0_min',
                    'mean_neg_1_mean',
                    'sd_diff_sd_0_mean_sd_1_mean']
    return df[top_features]