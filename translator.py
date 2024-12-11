"""
Generated by Gemini using this prompt.

You are a python programmer. Create a python program that will:

1. Read a large text file where each line is a message between two people.
2. Translate the message into English
3. Output a markdown table where the left column is the row number, the middle column is English translation, and the right column is the original text.

The file is very large and will have to be chunked.
"""
import pandas as pd
from google.cloud import translate_v2 as translate
from google.oauth2.service_account import Credentials

ROW_LIMIT = 100

def translate_text(text, api_key, target_language='en'):
    """
    Translates messages in a text file using the Google Cloud Translation API.

    Args:
        file_path: Path to the text file.
        project_id: Your Google Cloud project ID.

    Returns:
        A pandas DataFrame containing the row number, date, translated message, and original message.
    """
    credentials = Credentials.from_service_account_file('./.servicekey.json')
    client = translate.Client(credentials=credentials)

    data = []
    date = None
    row_num = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            row_num += 1
            line = line.strip()
            if not line:
                date = line.strip()
            else:
                line_parts = line.split('\t')

                if len(line_parts) == 3:    # Regular text line
                    # Extract the message from the line (adjust as needed)
                    message = line.split('\t')[2]

                    # Translate the message using the Google Cloud Translation API
                    result = client.translate(message, target_language=target_language)
                    translated_text = result['translatedText']

                    data.append([row_num, date, translated_text, message])
                else:
                    data.append([row_num, date, "", line])

            if row_num > ROW_LIMIT and ROW_LIMIT > 0:
                break
                    
    df = pd.DataFrame(data, columns=['Row Number', 'Date', 'Translated Message', 'Original Message'])
    return df

# Example usage:
file_path = input("Input file name: ")
project_id = input("API Key       : ")

df = translate_text(file_path, project_id)
with open('translator.md', 'w', encoding='utf-8') as f:
    f.write(df.to_markdown(index=False))
