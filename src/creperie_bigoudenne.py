from collections import defaultdict

R = "../Archives BTC 2022/La Crêperie Bigouden"

with open(f"{R}/produits.txt") as f:
    content = f.read().split('\n')


products = {k: int(v) for k, v in map(lambda l: l.split(';'), content)}

with open(f"{R}/tables.txt") as f:
    content = f.read().split('\n')

tables = {n: t for n, t in map(lambda l: l.split(';'), content)}

with open(f"{R}/commandes.txt") as f:
    content = f.read().split('\n')

commands = defaultdict(list)

for p, c in map(lambda l: l.split(';'), content):
    commands[p].append(c)

prices = defaultdict(int)

for name, command in commands.items():
    for p in command:
        prices[tables[name]] += products[p]


prices = {t: p / 100 for t, p in prices.items()}

print("max", max(prices.items(), key=lambda i: i[1]))
print("min", min(prices.items(), key=lambda i: i[1]))

print(sum(prices.values()))


print(sum(1 for t, n in prices.items() if n > 250))
