import unittest
from main import InverseRMQ


class TestInverseRMQ(unittest.TestCase):
    def setUp(self):
        self.inverseRMQ = InverseRMQ()

    def testSolve(self):
        self.assertEqual('Possible', self.inverseRMQ.possible(5, [1, 2, 4], [2, 4, 5], [3, 4, 5]))
        self.assertEqual('Impossible', self.inverseRMQ.possible(3, [1, 2, 3], [1, 2, 3], [3, 3, 3]))
        self.assertEqual('Possible', self.inverseRMQ.possible(600, [1, 101, 201, 301, 401, 501], [100, 200, 300, 400, 500, 600], [100, 200, 300, 400, 500, 600]))
        self.assertEqual('Impossible', self.inverseRMQ.possible(1000000000, [1234, 1234], [5678, 5678], [10000, 20000]))
        self.assertEqual('Possible', self.inverseRMQ.possible(8, [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], [4, 8, 2, 5, 6, 3, 7, 1]))
        self.assertEqual('Impossible', self.inverseRMQ.possible(1000000000, [1], [1000000000], [19911120]))
        self.assertEqual('Impossible', self.inverseRMQ.possible(1000000000, [1, 4], [3, 7], [3, 4]))
        self.assertEqual('Impossible', self.inverseRMQ.possible(1000000000, [1, 2], [3, 5], [3, 4]))

        if __name__ == '__main__':
            unittest.main()