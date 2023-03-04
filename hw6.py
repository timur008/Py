result = []
def divider(a, b):
    if b == 0:
        raise ZeroDivisionError("Unable to division by zero")
    if a != type(int) or b!= type(int):
        raise TypeError("Wrong data type")
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, 3: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)