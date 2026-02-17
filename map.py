def transform(x):
    return x ** 2

res = map(transform, [2, 3, 4])
print(list(res))