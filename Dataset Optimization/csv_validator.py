import csv

def validate_csv(file_path):
    try:
        # Open the CSV file with the specified path, using 'utf-8' encoding
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            num_columns = len(header)  # Determine the number of columns in the header
            for row in reader:
                # Check if each row has the correct number of columns
                if len(row) != num_columns:
                    return False
        return True  # Return True if the file is valid
    except Exception as e:
        # Print an error message if an exception occurs
        print(f"An error occurred: {e}")
        return False

# Specify the file path here
file_path = r'FILE_PATH'
is_valid = validate_csv(file_path)
print(f"Is the CSV file valid? {is_valid}")