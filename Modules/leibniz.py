def leibniz(terms): 
    acc=0
    num=4
    den=1

    for aterm in range(terms):
        nextterm = num/den*(-1)**aterm
        den = den+2
        acc = acc+nextterm
    return acc
