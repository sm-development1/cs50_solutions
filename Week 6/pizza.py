# Simple pizza menu lookup: read pizzas.csv and print price for a requested pizza.

import csv
import sys
from pathlib import Path

def load_menu(csv_path):
    menu = {}
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # expect columns: name, price
                name = row.get("name", "").strip().lower()
                price = row.get("price", "").strip()
                if name and price:
                    try:
                        menu[name] = float(price)
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Menu file not found: {csv_path}", file=sys.stderr)
        sys.exit(1)
    return menu

def main():
    # assume pizzas.csv is in the same folder
    csv_path = Path(__file__).parent / "pizzas.csv"
    menu = load_menu(csv_path)

    query = input("Pizza name: ").strip().lower()
    if query in menu:
        print(f"${menu[query]:.2f}")
    else:
        print("Not found")

if __name__ == "__main__":
    main()
