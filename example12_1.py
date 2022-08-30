class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key,[value]*3)

dd = DoppelDict(one=1)
print(dd)
dd['two']=2
print(dd)
dd.update(three=3)
print(dd)

