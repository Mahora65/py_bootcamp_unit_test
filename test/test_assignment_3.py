import unittest
import re
from tmp.assignment_3 import *

class TestAssignment3(unittest.TestCase):
    
    def test_exercise_01(self):
        self.assertIsInstance(exercise_01(), int, "This exercise should return integer")
        self.assertEqual(exercise_01(), 22, "This exercise should return 22")
    
    def test_exercise_02(self):
        self.assertIsInstance(exercise_02(), int, "This exercise should return integer")
        self.assertEqual(exercise_02(), 26, "This exercise should return 26")
    
    def test_exercise_03(self):
        self.assertIsInstance(exercise_03(), int, "This exercise should return integer")
        self.assertEqual(exercise_03(), 4, "This exercise should return 4")
    
    def test_exercise_04(self):
        self.assertIsInstance(exercise_04(), str, "This exercise should return string")
        self.assertEqual(exercise_04(), 'Aquatics', "This exercise should return Aquatics")
    
    def test_exercise_05(self):
        self.assertIsInstance(exercise_05(), str, "This exercise should return string")
        self.assertEqual(exercise_05(), 'Athletics', "This exercise should return Athletics")
    
    def test_exercise_06(self):
        self.assertIsInstance(exercise_06(), int, "This exercise should return integer")
        self.assertEqual(exercise_06(), 9850, "This exercise should return 9850")
    
    def test_exercise_07(self):
        self.assertIsInstance(exercise_07(), int, "This exercise should return integer")
        self.assertEqual(exercise_07(), 2000, "This exercise should return 2000")
    
    def test_exercise_08(self):
        self.assertIsInstance(exercise_08(), int, "This exercise should return integer")
        self.assertEqual(exercise_08(), 53, "This exercise should return 53")
    
    def test_exercise_09(self):
        self.assertIsInstance(exercise_09(), int, "This exercise should return integer")
        self.assertEqual(exercise_09(), 40, "This exercise should return 40")
    
    def test_exercise_10(self):
        self.assertIsInstance(exercise_10(), int, "This exercise should return integer")
        self.assertEqual(exercise_10(), 3, "This exercise should return 3")
    
    def test_exercise_11(self):
        self.assertIsInstance(exercise_11(), int, "This exercise should return integer")
        self.assertEqual(exercise_11(), 49, "This exercise should return 49")
    
    def test_exercise_12(self):
        self.assertIsInstance(exercise_12(), int, "This exercise should return integer")
        self.assertEqual(exercise_12(), 33, "This exercise should return 33")
    
    def test_exercise_13(self):
        self.assertIsInstance(exercise_13(), int, "This exercise should return integer")
        self.assertEqual(exercise_13(), 11, "This exercise should return 11")
    
    def test_exercise_14(self):
        self.assertIsInstance(exercise_14(), int, "This exercise should return integer")
        self.assertEqual(exercise_14(), 6, "This exercise should return 6")
    
    def test_exercise_15(self):
        self.assertIsInstance(exercise_15(), int, "This exercise should return integer")
        self.assertEqual(exercise_15(), 78, "This exercise should return 78")
    
    def test_exercise_16(self):
        self.assertIsInstance(exercise_16(), int, "This exercise should return integer")
        self.assertEqual(exercise_16(), 577, "This exercise should return 57")
    
    def test_exercise_17(self):
        self.assertIsInstance(exercise_17(), int, "This exercise should return integer")
        self.assertEqual(exercise_17(), 430, "This exercise should return 430")
    
    def test_exercise_18(self):
        self.assertIsInstance(exercise_18(), str, "This exercise should return string")
        self.assertEqual(exercise_18(), 'SZIVOS, Istvan', "This exercise should return SZIVOS, Istvan")
    
    def test_exercise_19(self):
        self.assertIsInstance(exercise_19(), int, "This exercise should return integer")
        self.assertEqual(exercise_19(), 7, "This exercise should return 7")
    
    def test_exercise_20(self):
        self.assertIsInstance(exercise_20(), int, "This exercise should return integer")
        self.assertEqual(exercise_20(), 29, "This exercise should return 29")
    
    def test_exercise_21(self):
        self.assertIsInstance(exercise_21(), str, "This exercise should return string")
        self.assertEqual(exercise_21(), 'GBR', "This exercise should return SZIVOS, Istvan")
    
    def test_exercise_22(self):
        self.assertIsInstance(exercise_22(), int, "This exercise should return interger")
        self.assertEqual(exercise_22(), 58593, "This exercise should return 58593")
    
    def test_exercise_23(self):
        self.assertIsInstance(exercise_23(), str, "This exercise should return string")
        self.assertEqual(exercise_23(), 'PHELPS, Michael', "This exercise should return PHELPS, Michael")
    
    def test_exercise_24(self):
        self.assertIsInstance(exercise_24(), str, "This exercise should return string")
        self.assertEqual(exercise_24(), 'LATYNINA, Larisa', "This exercise should return LATYNINA, Larisa")
    
    def test_exercise_25(self):
        self.assertIsInstance(exercise_25(), int, "This exercise should return integer")
        self.assertEqual(exercise_25(), 3, "This exercise should return 3")
    
    def test_exercise_26(self):
        self.assertIsInstance(exercise_26(), int, "This exercise should return integer")
        self.assertEqual(exercise_26(), 648, "This exercise should return 648")
    
    def test_exercise_27(self):
        self.assertIsInstance(exercise_27(), int, "This exercise should return integer")
        self.assertEqual(exercise_27(), 2004, "This exercise should return 2004")
    
    def test_exercise_28(self):
        self.assertIsInstance(exercise_28(), int, "This exercise should return integer")
        self.assertEqual(exercise_28(), 9772, "This exercise should return 9772")
    
    def test_exercise_29(self):
        self.assertIsInstance(exercise_29(), str, "This exercise should return string")
        self.assertEqual(exercise_29(), 'Vladimir', "This exercise should return Vladimir")
        self.assertEqual(re.search(" +", exercise_29()), None, "The return of this exercise should not have any withespace")
    
    def test_exercise_30(self):
        self.assertIsInstance(exercise_30(), str, "This exercise should return string")
        self.assertEqual(exercise_30(), 'Elena', "This exercise should return Elena")
        self.assertEqual(re.search(" +", exercise_30()), None, "The return of this exercise should not have any withespace")
        

if __name__ == '__main__':
    unittest.main()