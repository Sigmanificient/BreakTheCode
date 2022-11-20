from math import ceil

def rec() :
    a = 9541548745485187
    b = 0

    while (a >= 1):
        a -= ceil((a / 2) + 1)
        b += 1

        print(a, b)
    return a

print (rec())