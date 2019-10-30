from decimal import *

def square_rooting(a):
    getcontext().prec = 10
    return (Decimal(a) ** Decimal(0.5))