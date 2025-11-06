# Validate vanity plates according to CS50 rules.

def is_valid(s: str) -> bool:
    # Rule: 2–6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule: first two must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number_started = False

    for char in s:
        if char.isdigit():
            if char == "0" and not number_started:
                return False    # first number cannot be zero
            number_started = True
        else:
            if number_started:
                return False    # no letters after numbers

        if not char.isalnum():
            return False        # must be alphanumeric

    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
