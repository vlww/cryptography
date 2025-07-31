# encoded text:
# yeel omfx eamawwkmu, yhu nmmef bx tsc fxzt tlll lntigg! ljsg vukiye otu a urtralj mttscetvivill oaq il wpjd-dpopn qmj aks vooc-tkgadiye ohtk wucgfz vhx spaggf whrwb ott - igcwsvbpg urpycbpg mhp cfbimt czbw. ag il awqg vqnliocjxf a yoflvbpg yaefwk qf tregxbeitl tllxnlbgplux cnw czefbvioe daaxpcx.


text = input("Enter the encrypted message: ")


# Specified key
keyword = list("catalyst")

# Initialize some variables to be used later
keynums = []
repeat_key = []

temp_text = []
plaintext4 = []

symbol_location = []
symbol_value = []

# Just the alphabet :)
alf = list("abcdefghijklmnopqrstuvwxyz")

# We can think of the Vigenere like a lot of Caesar ciphers
# For example, the first letter of the keyword is c; that is like a shift of 2
# So first, we loop through the keyword and find the corresponding shifts
for i in range(len(keyword)):
    keynums.append(alf.index(keyword[i])) # this is a list of key numbers that correspond to the letters in the keyword

# Now we're going to delete the spaces/symbols in the ciphertext, but keep track of where they were so that we can add them back in later
# This is because we only want to assign a character in the keyword to letters of the ciphertext
for i in range(len(text)):
    if text[i] in alf: # these are alphabet letters that will be temporarily stored in a list, until they can be converted to plaintext
        temp_text.append(text[i]) 
    else: # these are spaces/symbols
        symbol_location.append(i) # a list of where the symbol/space was
        symbol_value.append(text[i]) # a list of what the symbol/space was

# Now that we know exactly how many letters were in the ciphertext (because that's all that was left in the temp_text), we can repeat the keyword so that it will be the same length too
for i in range(len(temp_text)):
    repeat_key.append(keynums[i%len(keyword)]) # these are the numbers that corresponded to the letters in the keyword, repeated so that there is one for each letter in the ciphertext
                                               # recall: the % symbol is the remainder function - it gives the remainder from division

# Now loop through the ciphertext to replace the cipher letters with plaintext
for i in range(len(temp_text)):
    if alf.index(temp_text[i]) - repeat_key[i] < 0: # check for if the shift in the alphabet pushes us "past" the end, and reset the indexing if needed
        plaintext4.append(alf[alf.index(temp_text[i]) - repeat_key[i] + 26])
    else: # no need for an extra shift :)
        plaintext4.append(alf[alf.index(temp_text[i]) - repeat_key[i]])

# Now put the spaces and characters that we took out back where they belong
for i in range(len(symbol_location)):
    plaintext4.insert(symbol_location[i],symbol_value[i])

# And print!
print("Ciphertext 4 decryption: ")
print("".join(plaintext4))