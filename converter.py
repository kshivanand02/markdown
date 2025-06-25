import argparse
import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: The file '{input_file}' does not exist.")
        return

    # Read Markdown content
    with open(input_file, 'r', encoding='utf-8') as md_file:
        markdown_text = md_file.read()

    # Convert to HTML using the markdown library
    html = markdown.markdown(markdown_text, extensions=['fenced_code', 'codehilite'])

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(f"<html><body>{html}</body></html>")

    print(f"✅ Successfully converted '{input_file}' to '{output_file}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown (.md) to HTML.")
    parser.add_argument("input", help="Path to the input .md file")
    parser.add_argument("output", help="Path to the output .html file")

    args = parser.parse_args()
    convert_markdown_to_html(args.input, args.output)
