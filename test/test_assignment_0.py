import unittest
from tmp.assignment_0 import *


class TestAssignment0(unittest.TestCase):
    def test_exercise_00(self):
        self.assertEqual(exercise_00(), (), "This should return ()")

    def test_exercise_01(self):
        self.assertEqual(exercise_01(), 0, "This should return 0")

    def test_exercise_02(self):
        self.assertEqual(exercise_02(), 1.0, "This should return 1.0")

    def test_exercise_03(self):
        self.assertEqual(exercise_03(), "Python", "This should return Python")

    def test_exercise_04(self):
        self.assertEqual(exercise_04(), [0], "This should return a list of 0")

    def test_exercise_05(self):
        self.assertEqual(exercise_05(), {"session": 1}, "This should return a dictionary {'session': 1}")

if __name__ == '__main__':
    unittest.main()
