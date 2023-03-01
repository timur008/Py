result = []

def divider(a, b):
    # if b == 0:
    #     raise ZeroDivisionError
    # if a != type(int):
    #     raise TypeError("kek")
    # else:
    return a/b

data = {10: 2, 2: 5, 18: 0, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)



print(result)
