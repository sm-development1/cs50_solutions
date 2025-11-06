# Clean a CSV of names and phone numbers:
# - Title-case names
# - Strip non-digit characters from phone numbers
# - Format 10-digit phones as XXX-XXX-XXXX
# Output cleaned CSV to stdout.

import csv
import re
import sys
from pathlib import Path

def clean_phone(raw):
    # keep digits only
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 10:
        return f"{digits[0:3]}-{digits[3:6]}-{digits[6:10]}"
    # if not 10 digits, return digits (or original raw if no digits)
    return digits if digits else raw

def clean_name(raw):
    return raw.strip().title()

def main():
    infile = Path(__file__).parent / "before.csv"
    if not infile.exists():
        print(f"Input file not found: {infile}", file=sys.stderr)
        sys.exit(1)

    # Read input CSV, detect headers
    with open(infile, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        if not fieldnames:
            print("No columns found in input.", file=sys.stderr)
            sys.exit(1)

        # We'll output same columns but clean name & phone if present
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Clean known columns if present
            if "name" in row:
                row["name"] = clean_name(row["name"])
            elif "Name" in row:
                row["Name"] = clean_name(row["Name"])

            if "phone" in row:
                row["phone"] = clean_phone(row["phone"])
            elif "Phone" in row:
                row["Phone"] = clean_phone(row["Phone"])

            writer.writerow(row)

if __name__ == "__main__":
    main()
