# Convert a fraction to a percentage and classify the fuel level.

def convert(fraction: str) -> int:
    """Convert fraction X/Y to a percentage."""
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    percentage = round((x / y) * 100)
    return percentage


def gauge(percentage: int) -> str:
    """Return E for <=1%, F for >=99%, else 'X%'."""
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
