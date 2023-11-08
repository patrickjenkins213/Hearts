from card import Card
from deck import Deck
from rank import Rank
from suit import Suit


def hearts_compare(card1, card2):
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
        if hearts_compare(card, win) == 1:
            win = card

    return trick.index(card)


class Hearts:
    def __init__(self):
        self.id = 7
        self.players = []

    @property
    def scores(self):
        return self.scores

    def add_player(self, player_id):
        if len(self.players) < 4:
            self.players.append(player_id)
            return True
        return False

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
