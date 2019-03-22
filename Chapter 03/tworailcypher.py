def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText: 
        if charCount % 2 == 0: 
            evenChars = evenChars + ch
        else: 
            oddChars = oddChars + ch
        charCount = charCount + 1 
    cipherTet = oddChars + evenChars
    return cipherText
