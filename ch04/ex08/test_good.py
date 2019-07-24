import unittest
from good import good


class Test_Good(unittest.TestCase):

    def test_good(self):
        expected = ['Harry', 'Ron', 'Hermione']
        self.assertEqual(good(), expected)


if __name__ == "__main__":
    unittest.main()
