def spaceRemover(phrase):
    smashedText = ""
    charCount = 0

    for ch in phrase:
        if ord(ch) !=32:
            smashedText = smashedText + ch
        charCount = charCount + 1
    return smashedText
