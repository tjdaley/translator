"""
Generated by Gemini using this prompt.

You are a python programmer. Create a python program that will:

1. Read a large text file where each line is a message between two people.
2. Translate the message into English
3. Output a markdown table where the left column is the row number, the middle column is English translation, and the right column is the original text.

I then modified the program, but Gemini got me started. --TJD
"""
import pandas as pd
from google.cloud import translate_v2 as translate
from google.oauth2.service_account import Credentials

ROW_LIMIT = 0  # Less than 1 means no limit--process the entire input file.
OUTPUT_FILE = 'translator.md'

def translate_text(text, target_language='en'):
    """
    Translates messages in a text file using the Google Cloud Translation API.

    Args:
        file_path: Path to the text file.
        project_id: Your Google Cloud project ID.

    Returns:
        A pandas DataFrame containing the row number, date, translated message, and original message.
    """
    try:
        credentials = Credentials.from_service_account_file('./.servicekey.json')
        client = translate.Client(credentials=credentials)
    except Exception as e:
        print("Error authenticating and authorizing:", str(e))
        exit(0)

    data = []
    date = None
    row_num = 0
    next_line_is_date = False
    date_stamp = ''
    time_stamp = ''

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            row_num += 1
            retry = True
            line = line.strip()
            if not line:
                next_line_is_date = True
                continue;
            elif next_line_is_date:
                date_stamp = line.strip()
                next_line_is_date = False
            else:
                line_parts = line.split('\t')

                if len(line_parts) == 3:    # Regular text line
                    # Extract the message from the line (adjust as needed)
                    time_stamp = line_parts[0]
                    originator = line_parts[1]
                    message = line_parts[2]

                    # Translate the message using the Google Cloud Translation API
                    while retry:
                        try:
                            result = client.translate(message, target_language=target_language)
                        except Exception as e:
                            print("Error translating line", row_num, ":", str(e))
                            action = input("Abort, Retry, or Ignore?")
                            if action == "A":
                                exit(0)
                            elif action == "R":
                                retry = True
                            elif action == "I":
                                retry = False
                                continue

                    translated_text = result['translatedText']

                    data.append([row_num, date_stamp, time_stamp, originator, translated_text, message])
                else:
                    data.append([row_num, "", "", "", "(short params)", line])

            if row_num > ROW_LIMIT and ROW_LIMIT > 0:
                break
                    
    df = pd.DataFrame(data, columns=['Row Number', 'Date', 'Time', 'Sender', 'Translated Message', 'Original Message'])
    return df

# Example usage:
file_path = input("Input file name: ")

df = translate_text(file_path)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(df.to_markdown(index=False))

print(f"{len(df)} rows of output saved to {OUTPUT_FILE}")
