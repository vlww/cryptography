import math

number = input("Enter the encrypted message: ")

for i in range(len(number)):
    print(number[len(number)-i-1])