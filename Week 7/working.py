import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM) to ([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    h1 = h1 % 12 + (12 if p1 == "PM" else 0)
    h2 = h2 % 12 + (12 if p2 == "PM" else 0)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

if __name__ == "__main__":
    main()
