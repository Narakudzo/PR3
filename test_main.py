import unittest
from unittest import TestCase

import main


class UnitTest(unittest.TestCase):
    def test_work_distribution_of_leaflets(self):
        a1 = main
        self.assertEqual(a1.work_distribution_of_leaflets(300), 307)

