import re

def compress_text_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Replace consecutive spaces with a single space
        content = re.sub(r'\s+', ' ', content)
        
        # Replace sequences of dashes longer than 5 with exactly 5 dashes
        content = re.sub(r'-{6,}', '-----', content)

        with open(output_file, 'w') as outfile:
            outfile.write(content)

        print(f"Compression complete. Compressed file saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace 'input.txt' and 'output.txt' with your file names
compress_text_file('translator.md', 'translator_min.md')
