# Render text as ASCII art using pyfiglet (simple default behavior).

from pyfiglet import Figlet

def main():
    text = input()
    fig = Figlet()
    # render and print ASCII art
    print(fig.renderText(text))

if __name__ == "__main__":
    main()
