import unittest
from .main import BowlingGame


class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, rolls, pins):
        for _ in range(rolls):
            self.game.roll(pins)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.game.score())

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.game.score())

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(300, self.game.score())

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)


if __name__ == '__main__':
    unittest.main()
