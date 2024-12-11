import re

def compress_text_file(input_file, output_file):
    try:
        # Open the file with UTF-8 encoding
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Process each line to compress spaces and dashes
        compressed_lines = []
        for line in lines:
            # Replace consecutive spaces with a single space
            line = re.sub(r'\s+', ' ', line)
            # Replace sequences of dashes longer than 5 with exactly 5 dashes
            line = re.sub(r'-{6,}', '-----', line)
            compressed_lines.append(line)

        # Write the compressed lines to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines('\n'.join(compressed_lines))

        print(f"Compression completed successfully. Output saved to '{output_file}'.")

    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify input and output files
input_file = "translator.md"  # Replace with your input file name
output_file = "translator_min.md"  # Replace with your output file name

compress_text_file(input_file, output_file)
