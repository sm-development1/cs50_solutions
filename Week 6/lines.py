# Count lines in a file and print the number of lines.

def main():
    filename = input("File name: ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            count = sum(1 for _ in f)
        print(f"Lines: {count}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
