with open("../Archives BTC 2022/Le Caddy breton/Facture.txt") as f:
    content = f.read().split('\n')


def parse(line):
    if line.count(' ') != 2:
        return 0

    q, _, p = line.split(' ')
    return int(q) * int(p)


print(sum(map(parse, content)))
