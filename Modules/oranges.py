def orangeCost(pounds):
    baseCost=.32*pounds
    if pounds <100:
        shipping = 7.5
    elif pounds >100:
        shipping=6
    print(baseCost+shipping)
