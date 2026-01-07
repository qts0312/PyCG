import json
import sys
import os

def format_json(input_file, output_file=None):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not output_file:
            output_file = "pretty_" + input_file

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False, sort_keys=True)

        print(f"Success! Formatted JSON saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python format_json.py <your_file.json>")
    else:
        format_json(sys.argv[1])