import math

jit = input("Enter the encrypted message: ")
tokens = jit.split(" ")

for token in tokens:
    if token == "|":
        print(" ", end="")
    elif all(char in "01" for char in token):  # Check if it's a binary number
        decimal = 0
        for i in range(len(token)):
            decimal += math.pow(2, i) * int(token[len(token) - i - 1])
        print(chr(int(decimal) + 64), end="")
    else:
        print(token, end="")
print()
