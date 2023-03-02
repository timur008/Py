result = []

def divider(a, b):
    if b == 0:
        raise ZeroDivisionError
    if a != type(int):
        raise TypeError("kek")
    return a/b

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
except (TypeError, IndexError, ZeroDivisionError) as error:
    print(error)
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
