import math
jit = input("Enter the encrypted message: ")
numbers_to_lock_in = jit.split(" ")
for number in numbers_to_lock_in:
    decimal = 0
    for i in range(len(number)):
        gurt = math.pow(2, i)
        decimal += gurt*int(number[len(number)-i-1])
    print(chr(int(decimal) + 64), end="")
print()