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
        self.assertEqual('Impossible', self.inverseRMQ.possible(93, [15, 20, 5, 19, 12, 9, 5, 42, 8, 44, 34, 6, 57, 5, 7, 25, 86, 13, 32, 45, 36, 25, 49, 64, 2, 23, 6, 17, 22, 39, 12, 5, 22, 52, 31, 28, 15, 68, 7, 36, 23, 23, 16, 3, 24, 13, 69, 58, 63, 4], [20, 73, 74, 62, 88, 69, 79, 58, 52, 80, 72, 92, 64, 92, 40, 72, 92, 14, 68, 82, 70, 80, 50, 79, 58, 27, 81, 82, 28, 55, 77, 66, 79, 79, 73, 42, 45, 80, 63, 90, 64, 58, 89, 67, 45, 46, 89, 65, 87, 39], [57, 19, 43, 20, 10, 71, 35, 9, 5, 68, 18, 35, 70, 38, 23, 20, 26, 1, 42, 12, 19, 35, 53, 38, 11, 2, 93, 13, 75, 44, 87, 18, 56, 79, 78, 32, 64, 13, 4, 83, 54, 72, 90, 71, 35, 35, 44, 38, 74, 87]))
        self.assertEqual('Possible', self.inverseRMQ.possible(759862069, [361173545, 37483817, 565176688], [469833196, 680874123, 581324681], [338987456, 683612743, 287711540]))
        self.assertEqual('Possible', self.inverseRMQ.possible(929603516, [573404032, 142441823], [593860708, 338287333], [572210444, 730871057]))
        self.assertEqual('Impossible', self.inverseRMQ.possible(999999, [1, 3], [2, 5], [2, 4]))

if __name__ == '__main__':
    unittest.main()