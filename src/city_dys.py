with open("../Archives BTC 2022/Cité d'Ys/coteBretonne.txt") as f:
    lines = f.read().split('\n')


line = ''.join(map(str.strip, lines))
blocks = []

M = len(lines)
i = 0

for c, i in enumerate(line):
    if i != 'V':
        continue

    blocks.append((c - 1, c, c + 1))


cache = 0

city = ''
cities = []
M = len(line)

for l, i, r in blocks:
    if cache not in (l, i, r):
        cities.append(city)
        city = ''

    if l > 0:
        city += line[l]

    city += line[i]

    if r < M:
        city += line[r]
    cache = r


def score(c):
    if 'D' in c:
        return 0

    if 'F' not in c:
        return 0

    return c.count('V')


m_c = max(cities, key=score)
print('->', cities.index(m_c))
