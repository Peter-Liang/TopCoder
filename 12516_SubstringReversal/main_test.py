import unittest
from main import SubstringReversal


class TestSubstringReversal(unittest.TestCase):
    def setUp(self):
        self.substrinReversal = SubstringReversal()

    def testSolve(self):
        self.assertEqual([2, 3], self.substrinReversal.solve("abdc"))
        self.assertEqual([0, 0], self.substrinReversal.solve("aabbcc"))
        self.assertEqual([0, 4], self.substrinReversal.solve("misof"))
        self.assertEqual([0, 2], self.substrinReversal.solve("ivan"))
        self.assertEqual([0, 13], self.substrinReversal.solve("thisseemstobeaneasyproblem"))


if __name__ == '__main__':
    unittest.main()