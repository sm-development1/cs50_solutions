from datetime import date
import inflect

p = inflect.engine()

def main():
    print(minutes_lived(input("Date of Birth: ")))

def minutes_lived(birthdate):
    try:
        year, month, day = map(int, birthdate.split("-"))
        dob = date(year, month, day)
    except ValueError:
        return "Invalid date"

    today = date.today()
    diff = today - dob
    minutes = diff.days * 24 * 60

    # Convert number to words and add "minutes"
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"

if __name__ == "__main__":
    main()
