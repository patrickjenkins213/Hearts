import unittest

from player import Player

cards = [
    'AS', 'KS', 'QS', 'JS', 'TS', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',
    'AH', 'KH', 'QH', 'JH', 'TH', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H',
    'AD', 'KD', 'QD', 'JD', 'TD', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',
    'AC', 'KC', 'QC', 'JC', 'TC', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C',
]

class TestPlayer(unittest.TestCase):
    def test_get_name(self):
        player = Player()
        name = player.get_name()
        self.assertTrue(type(name) is str)

    def test_get_hand(self):
        player = Player()
        hand = player.get_hand()
        self.assertEqual(player.get_hand(), [])

        hand = ['AS', 'KS', 'QS']
        player.add_cards_to_hand(hand)
        for card in player.get_hand():
            self.assertTrue(card in cards)

    def test_add_single_card_to_hand(self):
        player = Player()
        hand = ['AS']
        self.assertEqual(player.get_hand(), [])
        player.add_cards_to_hand(hand)
        self.assertEqual(player.get_hand(), hand)

    def test_add_multiple_cards_to_hand(self):
        player = Player()
        hand = ['2C', '5H', 'QD']
        self.assertEqual(player.get_hand(), [])
        player.add_cards_to_hand(hand)
        self.assertEqual(player.get_hand(), hand)

    def test_new_hand(self):
        player = Player()
        hand = ['AS', 'QS', 'AD']
        players = ['Paul', 'John', 'George', 'Ringo']
        player.new_hand(players)
        self.assertEqual(player.get_hand(), [])
        player.add_cards_to_hand(hand)
        player.new_hand(players)
        self.assertEqual(player.get_hand(), [])

    def test_pass_cards(self):
        player = Player()
        hand = ['AS', 'AD', '2C', '5C', '8D', '9H']
        player.add_cards_to_hand(hand)
        passed = player.pass_cards()
        self.assertEqual(type(passed), list)
        self.assertEqual(len(passed), 3)
        for card in passed:
            self.assertTrue(card in hand)
            self.assertTrue(card not in player.get_hand())


if __name__ == '__main__':
    unittest.main()
