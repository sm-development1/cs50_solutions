# Remove vowels from a string.

def shorten(word: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result


def main():
    text = input("Input: ")
    print("Output:", shorten(text))


if __name__ == "__main__":
    main()
