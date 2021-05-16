def intersect(a, b):
    c = []

    for item in a:
        if item in b:
            c.append(item)

    return c


def outersect(a, b):
    c = []

    for item in a:
        if item not in b:
            c.append(item)

    for item in b:
        if item not in a:
            c.append(item)

    return c


ll = [1, 2, 3, 4, 5]
ll2 = [3, 4, 5, 6, 7]

print(intersect(ll, ll2))
print(outersect(ll, ll2))
