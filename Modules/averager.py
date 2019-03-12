import math

def averager(N): 
    acc=0
    for x in range(1,N+1):
        acc=acc+x
        averageNumber = acc/N
    print(averageNumber)
