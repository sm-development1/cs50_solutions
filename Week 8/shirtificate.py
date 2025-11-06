from fpdf import FPDF

def main():
    name = input("Name: ")
    create_shirtificate(name)

def create_shirtificate(name):
    pdf = FPDF()
    pdf.add_page()

    # Title text
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 40, "CS50 Shirtificate", align="C")
    pdf.ln(20)

    # Insert shirt image (must be in same folder)
    pdf.image("shirtificate.png", x=10, y=60, w=190)

    # Add name on the shirt
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=55, y=140, txt=f"{name} took CS50")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
