text = input("Input: ")
vowels = "aeiouAEIOU"

print("Output: ", end="")
for char in text:
    if char not in vowels:
        print(char, end="")
print()
