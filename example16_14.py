def gen():
    yield from range(1,5)

result = list(gen())
print(result)