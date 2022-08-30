class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

import weakref

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red'), Cheese('Blue'), Cheese('Brie'),Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

sorted(stock.keys())
del catalog
sorted(stock.keys())
del cheese
sorted(stock.keys())
pass