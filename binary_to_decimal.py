import math

number = input("Enter the encrypted message: ")

decimal = 0
for i in range(len(number)):
    gurt = math.pow(2, i)
    decimal += gurt*int(number[len(number)-i-1])

print(int(decimal))