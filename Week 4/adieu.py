# Print the distinct vowels (a, e, i, o, u) that appear in input, in alphabetical order.

def main():
    s = input().lower()
    vowels = "aeiou"
    found = ""
    for v in vowels:
        if v in s:
            found += v
    print(found)

if __name__ == "__main__":
    main()
