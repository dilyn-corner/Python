import random

def keyGen():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    for i in range(len(alphabet)):
        ch = random.randint(0,25-i)
        key = key + alphabet[ch]
        alphabet = removeChar(alphabet,ch)
    return key
