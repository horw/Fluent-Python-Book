def chain(*iterables):
    for it in iterables:
        yield from it

s = 'abs'
t = tuple(range(3))
result = list(chain(s,t))
print(result)