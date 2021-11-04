import unittest
from tmp.assignment_2 import *

class TestAssignment2(unittest.TestCase):
    
    def test_exercises_00(self):
        self.assertEqual(exercise_00(), 99003)
    
    def test_exercises_01(self):
        self.assertEqual(exercise_01(), 15)
    
    def test_exercises_02(self):
        self.assertEqual(exercise_02(), 40254)
    
    def test_exercises_03(self):
        self.assertEqual(exercise_03(), 58574)
    
    def test_exercises_04(self):
        self.assertEqual(exercise_04(), 10468106)
    
    def test_exercises_05(self):
        self.assertEqual(exercise_05(),4959923)
    
    def test_exercises_06(self):
        self.assertEqual(exercise_06(),10121282)

    
    def test_exercises_07(self):
        self.assertEqual(exercise_07(),3977851)
    
    def test_exercises_08(self):
        self.assertEqual(exercise_08(), 39.5)
    
    def test_exercises_09(self):
        self.assertEqual(exercise_09(), 35.7)
    
    def test_exercises_10(self):
        self.assertEqual(exercise_10(), 242.0)
    
    def test_exercises_11(self):
        self.assertEqual(exercise_11(), 165.0)
    
    def test_exercises_12(self):
        self.assertEqual(exercise_12(), 260.1)
    
    def test_exercises_13(self):
        self.assertEqual(exercise_13(), 84.7)
    
    def test_exercises_14(self):
        self.assertEqual(exercise_14(), 251.4)
    
    def test_exercises_15(self):
        self.assertEqual(exercise_15(), 67.9)
    
    def test_exercises_16(self):
        self.assertEqual(exercise_16(), 13.9)
    
    def test_exercises_17(self):
        self.assertEqual(exercise_17(), 28.5)
    
    def test_exercises_18(self):
        self.assertEqual(exercise_18(), 15.5)
    
    def test_exercises_19(self):
        self.assertEqual(exercise_19(), 31.0)
    
    def test_exercises_20(self):
        self.assertEqual(exercise_20(), 66.5)
    
    def test_exercises_21(self):
        self.assertEqual(exercise_21(), 71.2)
    
    def test_exercises_22(self):
        self.assertEqual(exercise_22(), 58.5)
    
    def test_exercises_23(self):
        self.assertEqual(exercise_23(), 60.1)
    
    def test_exercises_24(self):
        self.assertEqual(exercise_24(), 18)
    
    def test_exercises_25(self):
        self.assertEqual(exercise_25(), 128.1)
    
    def test_exercises_26(self):
        self.assertEqual(exercise_26(), 62.0)
    
    def test_exercises_27(self):
        self.assertEqual(exercise_27(), 1.6)
    
    def test_exercises_28(self):
        self.assertEqual(exercise_28(), 4.9)

    def test_exercises_29(self):
        self.assertEqual(exercise_29(), 2.7)
    
    def test_exercises_30(self):
        self.assertEqual(exercise_30(), 6.0)

if __name__ == '__main__':
    unittest.main()
