from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)

print(d_proxy)
try:
    d_proxy[2]=5
except Exception as e:
    print(e)

d[2]='5'
print(d_proxy)