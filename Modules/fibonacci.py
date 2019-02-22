import math 

def fibonacci(n):
    a=1
    b=1
    for i in range(1,n-1):
        c=a+b
        a=b
        b=c
    print(c)
