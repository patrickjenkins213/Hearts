from card import Card
from deck import Deck
import player
from rank import Rank
from suit import Suit


def hearts_compare(card1, card2):
    """
    Compares cards two cards in a trick to see which one is greater.
    One of the cards will always be trump since trump is who led
    :param card1 Card:
    :param card2 Card:
    :param trump Suit:
    :return: 1 if card1 greater, -1 if card2 greater, 0 if same
    """
    if card1.suit is card2.suit:
        if card1.rank > card2.rank:
            return 1
        if card1.rank < card2.rank:
            return -1
        else:
            return 0

    return -1

def resolve_trick(trick):
    win = trick[0]
    for card in trick:
        #print(card, win, hearts_compare(card, win, trump))
        if hearts_compare(card, win) == 1:
            win = card

    return trick.index(card)

class Hearts(object):
    def __init__(self):
        self._players = [
            player.Player(),
            player.Player(),
            player.Player(),
            player.Player()
        ]

        self._scores = {
            self._players[0].get_name(): 0,
            self._players[1].get_name(): 0,
            self._players[2].get_name(): 0,
            self._players[3].get_name(): 0,
        }

    @property
    def scores(self):
        return self._scores

    def play_game(self):
        passing = [3, 1, 2, 0]
        hand_num = 0
        while max(list(self.scores.values())) < 100:
            for player in self._players:
                player.new_hand([player.get_name() for player in self._players])

            deck = Deck()
            deck.shuffle()
            for player in self._players:
                player.add_cards_to_hand([card.name for card in deck.deal(13)])

            for player in self._players:
                print(player.get_name(), player.get_hand())

            if passing[hand_num % 4]:
                cards_to_pass = [player.pass_cards() for player in self._players]
                for i, player in enumerate(self._players):
                    player.add_cards_to_hand(cards_to_pass[(i + passing[hand_num % 4]) % 4])
                    print(player.get_name(), player.get_hand())

            # Player with the Two of Clubs plays first
            lead = 0
            for i, player in enumerate(self._players):
                if Card(Rank.TWO, Suit.CLUBS).name in player.get_hand():
                    lead = i

            for _ in range(13):
                trick = []
                for i in range(4):
                    current_player = self._players[(lead + i) % 4]
                    trick.append(
                        Card.from_name(current_player.play_card(self._players[lead].get_name(), trick))
                    )

                winner = (lead + resolve_trick(trick)) % 4

                for player in self._players:
                    player.collect_trick(
                        self._players[lead].get_name(),
                        self._players[winner].get_name(),
                        [card.name for card in trick]
                    )

                print(f'Lead: {self._players[lead].get_name()}')
                print(f'Winner: {self._players[winner].get_name()}')
                print(f'[{trick[0]}, {trick[1]}, {trick[2]}, {trick[3]}]')

                lead = winner

            # TODO: refine this
            scores = [player.score() for player in self._players]
            for player in self._players:
                if max(scores) == 26:
                    if player.score() == 0:
                        self._scores[player.get_name()] += 26
                else:
                    self._scores[player.get_name()] += player.score()

            hand_num += 1

        print(self._scores)


if __name__ == '__main__':
    game = Hearts()
    game.play_game()
