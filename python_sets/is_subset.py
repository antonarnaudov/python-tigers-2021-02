from python_sets.is_empty import is_empty


def is_subset(a, b):
    return set(a).issubset(set(b))


x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5, 6]

print(is_subset(x, y))
