def difference(a, b):
    c = []
    for item in a:
        if item not in b:
            c.append(item)

    return c


ll = [1, 2, 3, 4, 5, 6]
ll2 = [4, 5, 6, 7, 8, 9]

# [ 1, 2, 3 ]
print(difference(ll, ll2))

