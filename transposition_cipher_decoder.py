# encoded text:
# g||attecbeuush|trpoksehal||rde2go|k|ecpon|s|vfr,0bdu,e|bwelal|s||pojclsoler|rcseiheere|d|tl5go|f5|up,flhen,chce|l||r|m|g5sh|knooaapeooay!|play|c,rsec||asimbs0|ub,0gno|iyodi|rel|gi1gecb1g|pom,dtflnerdbts|h|etose|e||ifi'wsea:0gne||rdr1n|p|o1udooac0|ars|,t|li||s|tdp.

# Note: we need to import an extra library here to help with the rounding
import math

# Text to decrypt
ciphertext3 = input("Enter the encrypted message: ")
# Specified key
key = 4

# Just the alphabet :)
alf = list("abcdefghijklmnopqrstuvwxyz")

# Intialize some variables to be used later
row_in_table = []
decrypted_text = []
reformatted_text = []
plaintext3 = []

# Number of rows that we'll need in our table
# Note: the "ceil" function always rounds up
# If we had a partial row but rounded down, the message wouldn't fit anymore!
num_row = math.ceil(len(ciphertext3)/key)


# Since we rounded up, find out how many columns of the table are actually full
full_columns = key - (num_row*key - len(ciphertext3))

# Translate the transposed line of characters back into the original line of characters
# As an intermediate step, we have to recreate the table that the message was organized into
for i in range(num_row):
    if full_columns != key and i == num_row-1: # this is how we deal with the partial row that occurs if the message didn't fit into the table perfectly
                                               # recall: indexing is organized as start:stop:step
        row_in_table = ciphertext3[i:num_row*full_columns:num_row]
    else: # otherwise, we need a full row
        row_in_table = ciphertext3[i:num_row*full_columns:num_row] + ciphertext3[num_row*full_columns+i:len(ciphertext3):num_row-1]
                                                                   # ^ the step decreases by 1 because the last row is empty in these columns
    decrypted_text.append(row_in_table) # write the rows in order to get the original text
    
# Filter out where all the spaces were
reformatted_text = "".join(decrypted_text) # this makes it easier to loop through all the characters
                                           # (decrypted_text still has everything separated based on the row it was in)
for i in range(len(reformatted_text)):
    if reformatted_text[i] == "|": # this symbol was used to represent spaces, so when it comes up, we replace it with a space
        plaintext3.append(" ")
    else: # if it isn't a space, just leave it. The message should be decrypted at this point.
        plaintext3.append(reformatted_text[i])

# Print!
print("Ciphertext 3 decryption: ")
print("".join(plaintext3))