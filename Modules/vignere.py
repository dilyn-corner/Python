def vignereIndex(keyLetter,plainTextLetter):
    keyIndex = letterToindex(keyLetter)
    ptIndex = letterToIndex(plainTextLetter)
    newIdx = (ptIndex + keyIndex) % 26
    return indexToLetter(newIdx)

def encryptVignoere(key,plainText):
    cipherText = ""
    keyLen = len(key)
    for i in range(len(plainText)):
        ch = plainText[i]
        if ch == ' ':
            cipherText = cipherText + ch
        else:
            cipherText = cipherText + cignereIndex(key[i%keyLen],ch)
    return cipherText
