# encoded text:
# 11 1111 1110 111 10010 1 10100 10101 1100 1 10100 1001 1111 1110 10011 ! | 11001 1111 10101 | 100 1001 100 | 1001 10100 ! | 11 1001 10000 1000 101 10010 10100 101 11000 10100 | 10011 1 1101 10000 1100 101 | 10100 10111 1111 | 10101 10011 101 10011 | 10100 1000 101 | 11 1 101 10011 1 10010 | 11 1001 10000 1000 101 10010 , | 10111 1001 10100 1000 | 1011 101 11001 | = | 10100 1000 10010 101 101 .

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
