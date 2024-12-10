import pandas as pd
from googletrans import Translator

def translate_and_table(file_path, chunksize=10000):
  """Reads a large text file, translates messages, and generates a Markdown table.

  Args:
    file_path: Path to the text file.
    chunksize: Number of lines to process in each chunk.

  Returns:
    A pandas DataFrame containing the row number, English translation, and original text.
  """

  df = pd.DataFrame(columns=['Row Number', 'English Translation', 'Original Text'])

  with pd.read_csv(file_path, chunksize=chunksize) as reader:
    for chunk in reader:
      chunk['English Translation'] = chunk.apply(lambda row: Translator().translate(row['Original Text']).text, axis=1)
      df = pd.concat([df, chunk], ignore_index=True)

  # Create a Markdown table
  markdown_table = df.to_markdown(index=False, numalign='left', stralign='left')

  return markdown_table

# Example usage:
file_path = 'your_large_text_file.txt'
markdown_table = translate_and_table(file_path)

# Print or save the Markdown table
print(markdown_table)
# Or, save it to a file:
with open('translated_messages.md', 'w') as f:
  f.write(markdown_table)
