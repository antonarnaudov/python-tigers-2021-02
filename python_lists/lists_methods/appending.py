ll = []

print(ll)

ll.append(97)

ll.append('anything')

ll.append(True)

ll.append([1, 2, 3])

ll.insert(1, 'alabala')

print(ll)

for item in ll:
    print(type(item))
