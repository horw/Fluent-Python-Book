

class test:

    def __init__(self):
        pass

    def __add__(self, other):
        print('add')
        return other

    def __radd__(self, other):
        print('radd')
        return other

print( test() + 1 )
print(1 + test())
