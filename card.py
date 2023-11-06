from rank import Rank
from suit import Suit


class Card(object):
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @classmethod
    def from_name(cls, name):
        for rank in Rank:
            if rank.label == name[:-1]:
                r = rank
        for suit in Suit:
            if suit.label == name[-1]:
                s = suit

        return Card(r, s)

    def __repr__(self):
        return f'Card({self._rank.label}, {self._suit.label})'

    def __str__(self):
        return f'{self._rank.label}{self._suit.label}'

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    @property
    def name(self):
        return self.rank.label + self.suit.label

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit
