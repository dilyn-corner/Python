def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2 
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars): 
        plainText = plainText + evenChars[-1]

    return plainText
