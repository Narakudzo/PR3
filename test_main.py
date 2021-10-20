import unittest
from unittest import TestCase

import main


class UnitTest(unittest.TestCase):
    def test_work_distribution_of_leaflets(self):
        a1 = main
        self.assertEqual(a1.work_distribution_of_leaflets(300), 307)


class Test(TestCase):
    def test_work_programming(self):
        a2 = main
        self.assertEqual(a2.work_programming(200), 215)

if __name__ == "__main__":
    u = UnitTest()
    u.test_work_distribution_of_leaflets()
    u2 = Test()
    u2.test_work_programming()
