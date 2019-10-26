import random

from card import Card
from rank import Rank
from suit import Suit

class Deck(object):
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in Suit for rank in Rank]

    @property
    def size(self):
        return len(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, n=1):
        return [self._cards.pop() for _ in range(n)]
