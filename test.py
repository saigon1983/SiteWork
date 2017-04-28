a = [3,4,5,6,5,4,5,4]

def removeAll(array, item):
    for i in range(array.count(item)): array.remove(item)

removeAll(a, 4)
print(a)