# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
# count = Counter(7)
# # for elem in count:
# #      print(elem)
# print(count.__next__())
# print(count.__iter__())
# print(next(count))
# print(next(count))
# print(iter(count))
# print(next(count))
# print(next(count))


def raise_to_degrees(number, max_degree):
    i = 1
    for _ in range(max_degree):
        yield number**1
        i += 1
res = raise_to_degrees(1222345, 500)
print(res)
for _ in res:
    print(_)