def substitutionEncrypt(plainText,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText: 
        idx = alphabet.find(ch)
        chipherText = cipherText + key[idx]
    return cipherText
