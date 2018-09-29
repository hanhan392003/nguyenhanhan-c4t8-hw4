import math
n = int(input("Please input a number : "))
i = 0

while True :
    n_fabs = math.fabs(n)
    quotient = n_fabs // (10**i)
    quotient_fabs = math.fabs(quotient)

    if quotient_fabs > 0 :
        i += 1
    elif quotient_fabs == 0:
        print(i)
        break
    