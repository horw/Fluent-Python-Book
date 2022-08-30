import abc
import random


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""

    @abc.abstractmethod
    def pick(self):
        """
        Remove item at random, returning it.

        This method should raise
        'LookupError' when the instance is empty
        :return:
        """

    def loaded(self):
        """Return 'True' if there's at least 1 item, 'False' otherwise"""

    def inspect(self):
        """Return a sorted tuple with the items currently inside"""
        items = [ ]
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

class Fake(Tombola):
    def load(self):
        pass
    def pick(self):
        return 13

class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._item = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        self.pick