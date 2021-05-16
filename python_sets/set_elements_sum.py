def set_elements_sum(a, b):
    c = []

    for i in range(len(a)):
        result = a[i] + b[i]
        c.append(result)

    return c


ll = [1, 2, 3, 4, 5]
ll2 = [3, 4, 5, 6, 7]

print(set_elements_sum(ll, ll2))
# [4, 6, 8, 10, 12]
