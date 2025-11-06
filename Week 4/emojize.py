# Convert emoji aliases or common shortcuts to actual emoji using the emoji library.

import emoji

def main():
    text = input()
    # language="alias" lets emoji library translate aliases like :smile: and some shortcuts
    print(emoji.emojize(text, language="alias"))

if __name__ == "__main__":
    main()
