import csv
import pandas as pd
import json

def read_json(file_path):
    # Initialize a dictionary to store the data for the DataFrame
    df_data = {
        'index': [],
        'text': [],
        'company': [],
        'positive': [],
        'negative': [],
        'notr': []
    }

    # Mapping from Turkish tags to English column names
    translate_json = {
        'FIRMA': 'company',
        'POZITIF': 'positive',
        'NEGATIF': 'negative',
        'NOTR': 'notr'
    }

    # Open and read the JSON file
    with open(file_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)

        # Iterate through each item in the JSON data
        for i in data['data']:
            # Append the page index and text to the corresponding lists
            df_data['index'].append(i['page'])
            df_data['text'].append(i['text'])
            
            # Temporary dictionary to hold annotation data
            temp_data = {
                'company': [],
                'positive': [],
                'negative': [],
                'notr': []
            }

            annotations = i['annotations']

            # Process each annotation in the item
            for x in annotations:
                try:
                    # Translate the tag to the English version and append the text
                    eng_version = translate_json[x['tag']]
                    temp_data[eng_version].append(x['text'])
                except KeyError:
                    print('Error in this data:', end='')
                    print(i)
            
            # Remove duplicates and join the values for each annotation type
            for b in temp_data:
                if temp_data[b]:
                    del_dup = list(set(temp_data[b]))
                    new_value = '|'.join(del_dup)
                    df_data[b].append(new_value)
                else:
                    df_data[b].append('')

    # Convert the dictionary to a DataFrame and save it as a CSV file
    df = pd.DataFrame(df_data)
    df.to_csv('converted_dataset.csv', index=False)
    
    return True

# Specify the path to the JSON file
file_path = r'ENTER_FILE_PATH'

# Read the JSON file and process the data
df_data = read_json(file_path)
