# print(type(ll))
# print(len(ll))
#
# print(ll)
#
# result = 0
# ll2 = [1, 2, 3, 4, 5]
#
# for item in ll2:
#     result += item
#     print(item)
#
# print(result)

# ll = [1, 2, 3, 4, 5, 'Baba', 'Dqdo', True, False, 2.23]  # List



# result = 0
#
# for item in ll + ll2:
#     result += item
#     print(item)
#
# print()
# print(len(ll))

ll = [1, 2, 3, 4, 5]
ll2 = [6, 7, 8, 9, 10]
result = 0

for i in range(len(ll)):
    result += ll[i] + ll2[i]
    print(ll[i], ll2[i])
    print(result)
    print()

print(result)