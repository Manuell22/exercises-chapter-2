import math as m
def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,round(m.sqrt(n))+1): 
        if n%i==0 and n != i:
            return False
    return True