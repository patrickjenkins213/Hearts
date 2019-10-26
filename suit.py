from enum import IntEnum

class Suit(IntEnum):
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

    SPADES = (1, 'S')
    HEARTS = (2, 'H')
    DIAMONDS = (3, 'D')
    CLUBS = (4, 'C')
