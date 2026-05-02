"""
Email Extractor Script

This script extracts all email addresses from a given text file
and saves them into a separate output file.

Usage:
    python email_extractor.py input.txt output.txt
"""

import re
import sys


def extract_emails(text):
    """
    Extracts email addresses from a given text using regex.
    """
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)


def read_file(file_path):
    """
    Reads and returns content from a file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


def write_file(file_path, emails):
    """
    Writes extracted emails to a file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for email in emails:
            file.write(email + '\n')


def main():
    """
    Main function to run the script.
    """
    if len(sys.argv) != 3:
        print("Usage: python email_extractor.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    text = read_file(input_file)
    emails = extract_emails(text)

    if emails:
        write_file(output_file, emails)
        print(f"{len(emails)} email(s) extracted and saved to '{output_file}'.")
    else:
        print("No email addresses found.")


if __name__ == "__main__":
    main()
