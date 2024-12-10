"""
Generated by Gemini using this prompt.

You are a python programmer. Create a python program that will:

1. Read a large text file where each line is a message between two people.
2. Translate the message into English
3. Output a markdown table where the left column is the row number, the middle column is English translation, and the right column is the original text.

The file is very large and will have to be chunked.
"""
import pandas as pd
from googletrans import Translator

def process_messages(file_path):
    """
    處理訊息檔案，將訊息轉換成 DataFrame 格式

    Args:
        file_path: 訊息檔案的路徑

    Returns:
        pandas.DataFrame: 包含行號、日期、翻譯訊息和原始訊息的 DataFrame
    """

    data = []
    date = None
    row_num = 1

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                date = line.strip()
            else:
                # Google Translate
                parts = line.split('\t')
                if len(parts) < 3:
                    data.append([row_num, date, "", " ".join(parts)])
                    continue
                if len(parts.strip()) < 1:
                    data.append([row_num], date, "", parts[2]])
                    continue
                translated_text = Translator().translate(parts[2]).text
                data.append([row_num, date, translated_text, parts[2]])
                row_num += 1

    df = pd.DataFrame(data, columns=['Row Number', 'Date', 'Translated message', 'Original Message'])
    return df

file_path = input("Input file name: ")
df = process_messages(file_path)
print(df)
