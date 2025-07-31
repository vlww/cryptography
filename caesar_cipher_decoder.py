# encoded text:
# kfzb tloh zxqxivpqp, vlr'ob exictxv alkb! zfmeboqbuq pxjmib 3 rpbp qeb qoxkpmlpfqflk zfmebo, xka qeb hbv fp clro. fq jxv yb qofzhv! mxv zxobcri xqqbkqflk ql vlro fkabufkd. zfmeboqbuq pxjmib 4 rpbp qeb sfdbkbob zfmebo tfqe hbv = zxqxivpq. zebzh qeb zfmebo zebxq pebbq clo x efkq lk elt ql plisb qefp lkb!

text = input("Enter the encrypted message: ")

shift = -3
result = ""

for char in text:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - base - shift) % 26 + base)
    else:
        result += char 

print(result)



