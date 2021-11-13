import unittest
import math



class Stats(unittest.TestCase):

    def test_mean(self):
        test_cases = [

        ]

        for expected, param in test_cases:
            with self.subTest(f"{param} -> {expected}"):
                actual = zmean(param)
                self.assertEqual(expected, actual)
