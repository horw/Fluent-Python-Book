x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

from collections import namedtuple

City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo', 'Japan', 45.333, (1,2))
print(tokyo)