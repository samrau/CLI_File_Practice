poem_file = open('input_file.txt', encoding='utf-8')
content = poem_file.read()
print(content)
poem_file.close()

import argparse
import base64
import shutil

# This part capitalizes the texts
def capitalize_text(text):
    return text.upper()

# encodes base64
def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def main():
    parser = argparse.ArgumentParser(description="Text manipulation CLI program.")
    parser.add_argument("input_file", help="Path to input text file.")
    parser.add_argument("output_file", help="Path to the output text file.")
    parser.add_argument("-c", "--capitalize", action="store_true", help="Change to capital letters")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode the content to base64")

    args = parser.parse_args()

    shutil.copyfile(args.input_file, args.output_file)

    with open(args.output_file, "r") as file:
        text = file.read()
    
    if args.capitalize:
        text = capitalize_text(text)
    if args.encode:
        text = encode_base64(text)

    with open(args.output_file, 'w') as file:
        file.write(text)

if __name__ == "__main__":
    main()
