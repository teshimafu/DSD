import unittest
from amount_compare import amount_compare


class Main_Test(unittest.TestCase):

    def test_amount_compare(self):
        test_cases = {6: 'too low', 7: 'just right', 8: 'too high'}
        for num, text in test_cases.items():
            self.assertEqual(amount_compare(num), text)


if __name__ == "__main__":
    unittest.main()
