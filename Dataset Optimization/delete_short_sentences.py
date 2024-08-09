import pandas as pd
import numpy as np

def filter_data(input_file, output_file):
    # Read the data from the CSV file
    df = pd.read_csv(input_file)

    # Handle missing or empty values
    df['text'] = df['text'].fillna('')  # Replace NaN values with an empty string

    # Filter rows based on the word count in the 'text' column
    df['word_count'] = df['text'].apply(lambda x: len(x.split()) if isinstance(x, str) else 0)
    filtered_df = df[df['word_count'] >= 4]

    # Drop the unnecessary column
    filtered_df = filtered_df.drop(columns=['word_count'])

    # Write the results to a new CSV file
    filtered_df.to_csv(output_file, index=False)

# Example usage
input_file = 'ENTER_INPUT_FILE'  # Replace with your input file path
output_file = 'ENTER_OUTPUT_FILE'  # Replace with your output file path
filter_data(input_file, output_file)