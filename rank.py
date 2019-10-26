from enum import IntEnum

class Rank(IntEnum):
    def __new__(cls, value, label):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj._label = label

        return obj

    def __repr__(self):
        return f'<{self.__class__.__name__}.{self.name}>'

    @property
    def label(self):
        return self._label

    TWO = (1, '2')
    THREE = (2, '3')
    FOUR = (3, '4')
    FIVE = (4, '5')
    SIX = (5, '6')
    SEVEN = (6, '7')
    EIGHT = (7, '8')
    NINE = (8, '9')
    TEN = (9, 'T')
    JACK = (10, 'J')
    QUEEN = (11, 'Q')
    KING = (12, 'K')
    ACE = (13, 'A')
