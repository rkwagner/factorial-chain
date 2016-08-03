from math import factorial

fs = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

total = 0
for n in range(1, 1000001):
    p = []
    q = n
    while q not in p:
        p.append(q)
        q = sum(fs[int(d)] for d in str(q))

    if len(p) == 60:
        total += 1
print total
