__author__ = 'Peter Liang'
import unittest
from main import BubbleSortWithReversals


class TestBubbleSortWithReversals(unittest.TestCase):
    def setUp(self):
        self.target = BubbleSortWithReversals()

    def testGetMinSwap(self):
        self.assertEqual(0, self.target.getMinSwaps([6, 8, 8, 7, 7], 1))
        self.assertEqual(3, self.target.getMinSwaps([7, 2, 2, 13, 5, 5, 2], 2))
        self.assertEqual(12, self.target.getMinSwaps([12, 5, 1, 10, 12, 6, 6, 10, 6, 8], 2))
        self.assertEqual(1, self.target.getMinSwaps([2, 3, 1], 2))
        self.assertEqual(22, self.target.getMinSwaps([482, 619, 619, 601, 660, 660, 691, 691, 77, 77, 96, 77], 9))


if __name__ == '__main__':
    unittest.main()