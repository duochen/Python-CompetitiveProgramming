intArray = input().removesuffix(']')
intArray = intArray.removeprefix('[')
intArray = intArray.replace(' ', '')
intArray = list(map(int, intArray.split(',')))
result = []
total = 1

for i in range(len(intArray)):
    for a in intArray[:i]:
        total *= a
    for b in intArray[i+1:]:
        total *= b
    result.append(total)
    total = 1
print(result)