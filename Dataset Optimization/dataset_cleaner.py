import pandas as pd
import re
import string
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import unicodedata
import inflect

# Stop words and lemmatizer (assuming they are already downloaded)
stop_words = set(stopwords.words('turkish'))
lemmatizer = WordNetLemmatizer()

def number_to_words(n):
    ones = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    teens = ["on", "on bir", "on iki", "on üç", "on dört", "on beş", "on altı", "on yedi", "on sekiz", "on dokuz"]
    tens = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    thousands = ["", "bin", "milyon", "milyar"]

    def parse_number(n):
        if n < 10:
            return ones[n]
        elif 10 <= n < 20:
            return teens[n - 10]
        elif 20 <= n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
        elif 100 <= n < 1000:
            return ones[n // 100] + " yüz" + ("" if n % 100 == 0 else " " + parse_number(n % 100))
        elif 1000 <= n < 1000000:
            return parse_number(n // 1000) + " bin" + ("" if n % 1000 == 0 else " " + parse_number(n % 1000))
        elif 1000000 <= n < 1000000000:
            return parse_number(n // 1000000) + " milyon" + ("" if n % 1000000 == 0 else " " + parse_number(n % 1000000))
        else:
            return n

    return parse_number(n).strip()

def convert_numbers_to_words(text):
    def replace(match):
        number = int(match.group())
        return number_to_words(number)
    
    return re.sub(r'\d+', replace, text)



def clean_text(text):
    """
    Cleans text by removing HTML tags, converting to lowercase,
    removing links, punctuation, numbers, stop words, and lemmatizing.
    """

    # HTML tag removal
    text = BeautifulSoup(text, "html.parser").get_text()

    # Lowercase conversion
    text = text.lower()

    # Link removal
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Sayıları yazıya çevir
    text = convert_numbers_to_words(text)
    
    # Change Special Characters and digits with space
    text = text.translate(str.maketrans('', '', string.punctuation + '«»“”‘’'))
    
    # Convert multiple spaces into a single space
    text = re.sub(r'\s+', ' ', text).strip()

    # Stop word removal and lemmatization
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    # Fix whitespace
    text = ' '.join(tokens)

    return text

with open('text.txt', 'r', encoding='UTF-8') as file:
    data = file.read().split('\n')

content = {'text': data}

df = pd.DataFrame(content)

# Text cleaning
df['clean_text'] = df['text'].apply(clean_text)

# Save the DataFrame with the clean text column
df.to_csv('cleaned_text.csv', index=False)  # Save to CSV file
# df.to_excel('cleaned_text.xlsx', index=False)  # Uncomment to save to Excel

print(df['clean_text'])  # Print for verification (optional)
