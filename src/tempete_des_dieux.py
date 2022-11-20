from math import ceil


def rec():
    with open("../Archives BTC 2022/Tempête des Dieux/JDD_tempete.txt") as f:
        a = int(f.read())
    b = 0

    while a >= 1:
        a -= ceil((a / 2) + 1)
        b += 1

        print(a, b)
    return a


print(rec())
