with open("../Archives BTC 2022/Cité d'Ys/coteBretonne.txt") as f:
    lines = f.read().split('\n')


line = ''.join(map(str.strip, lines))
print(line)
