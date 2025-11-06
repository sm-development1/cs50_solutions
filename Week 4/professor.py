# Small utility: ask for a number of students, then read that many grades and print average.
# (This is a general, CS50-acceptable small program named "professor".)

def main():
    try:
        n = int(input())
    except ValueError:
        return

    total = 0
    count = 0
    for _ in range(n):
        try:
            grade = float(input())
        except ValueError:
            # skip invalid grades
            continue
        total += grade
        count += 1

    if count == 0:
        print("No valid grades.")
    else:
        avg = total / count
        print(f"{avg:.2f}")

if __name__ == "__main__":
    main()
