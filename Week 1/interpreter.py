# Get user input
expression = input("Expression: ")

# Split into parts
x, operator, z = expression.split()

# Convert to floats
x = float(x)
z = float(z)

# Perform the operation
if operator == "+":
    print(x + z)
elif operator == "-":
    print(x - z)
elif operator == "*":
    print(x * z)
elif operator == "/":
    print(x / z)
    