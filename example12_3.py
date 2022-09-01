import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] *2 )


dd = DoppelDict2(one=1)
print(dd)

dd.update(three=3)
print(dd)