import collections
import random

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))
print(deck[3])
print(random.choice(deck))

sorting_range = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def get_sorted_weight(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(sorting_range) + sorting_range[card.suit]


for card in sorted(deck, key=get_sorted_weight):
    print(card)