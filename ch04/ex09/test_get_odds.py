import unittest
from get_odds import get_odds


class Test_Good(unittest.TestCase):

    def test_get_odds(self):
        expected = [number for number in range(10) if number % 2 == 1]
        self.assertEqual(get_odds(), expected)


if __name__ == "__main__":
    unittest.main()
