import re


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):
    pattern = r"(\+91[\s-]?)?[6-9]\d{9}"
    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_name(text):
    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 2 and len(line.split()) <= 4:

            if "@" not in line and not any(char.isdigit() for char in line):

                return line

    return "Not Found"