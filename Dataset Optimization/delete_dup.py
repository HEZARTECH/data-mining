import pandas as pd

def remove_duplicates(file_path, column_name, output_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Remove rows that are duplicates in the specified column
    df_cleaned = df.drop_duplicates(subset=[column_name], keep='first')

    # Write the cleaned data to a new CSV file
    df_cleaned.to_csv(output_path, index=False)

# Usage
file_path = r'INPUT_FILE_PATH'  # Path to the original CSV file
column_name = 'ENTER_COLUMN_NAME'  # Name of the column to check for duplicates
output_path = r'OUTPUT_FILE_PATH'  # Path to the output CSV file

remove_duplicates(file_path, column_name, output_path)