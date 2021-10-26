import unittest
from tmp.assignment_1 import *


class TestAssignment1(unittest.TestCase):
    def test_exercise_00(self):
        """
        Test exercise_00 that return rectangle after given hight and width
        """
        self.assertEqual(exercise_00(10,20), 200, "Should be 200")
        self.assertEqual(exercise_00(0,0), 0, "Should be 0")
        self.assertEqual(exercise_00(-20, 10), -200, "Should be -200")
        self.assertEqual(exercise_00(20, -10), -200, "Should be -200")
    
    def test_exercise_01(self):
        """
        Test the XOR operation on exercise_01
        """
        self.assertFalse(exercise_01(True, True), "Should be False")
        self.assertTrue(exercise_01(True, False), "Should be True")
        self.assertTrue(exercise_01(False, True), "Should be True")
        self.assertFalse(exercise_01(False, False), "Should be False")
        
    def test_exercise_02(self):
        """
        Test seconds converter function on exercise_02
        """
        self.assertEqual(exercise_02(1,1,1), 3661, "Should be 3661")
        self.assertEqual(exercise_02(13, 5, 19), 47119, "should be 47119")
        self.assertEqual(exercise_02(0,0,48), 48, "Should be 48")
        self.assertEqual(exercise_02(0,3,0), 180, "Should be 180")
        self.assertEqual(exercise_02(4,0,0), 14400, "Should be 14400")
        self.assertEqual(exercise_02(0,0,0), 0, "Should be 0")

    def test_exercise_03(self):
        """
        Test the sum of function exercise_03 after given an integer.
        """
        self.assertEqual(exercise_03(3), 18, "Should be 18")
        self.assertEqual(exercise_03(0), 0, "Should be 0")
        self.assertEqual(exercise_03(-3), 0, "Should be 0")
    
    def test_exercise_04(self):
        """
        Test the exercise_04 function that they return the first and last letter, 
        if the input is empty string then return empty string.
        """
        self.assertEqual(exercise_04("Python"), "Pn", "should be Pn")
        self.assertEqual(exercise_04(""), "", "should be empty string")
        self.assertEqual(exercise_04("emlyon"), "en", "should be en")
    
    def test_exercise_05(self):
        """
        Test exercise_05 with given string reverse it and insert it into the template sentence
        """
        self.assertEqual(exercise_05("Paris"), 'The reverse of Paris is siraP!')
        self.assertEqual(exercise_05("Python"), 'The reverse of Python is nohtyP!')
        self.assertEqual(exercise_05("emlyon"), 'The reverse of emlyon is noylme!')
        
    
    def test_exercise_06(self):
        """
        Test exercise_06 which will return True if the letters in the string is unique.
        """
        self.assertTrue(exercise_06("Python"), "This should be True")
        self.assertFalse(exercise_06("PPython"), "This should be False")
        self.assertFalse(exercise_06("Pythonn"), "This should be False")
        self.assertTrue(exercise_06("Ppython"), "This should be True")
        self.assertTrue(exercise_06("Ppy-thon"), "This should be True")
    
    def test_exercise_07(self):
        """
        Test exercise_07 which will return True if the string is a palindrome.
        """
        self.assertTrue(exercise_07("tattarrattat"), "This should True")
        self.assertFalse(exercise_07("Python"), "this should be False")
    
    def test_exercise_08(self):
        """
        Test exercise_08 that will sorted the list of 3 number and return the middle index value
        """
        self.assertEqual(exercise_08(9,5,6), 6, "This should be 6")
        self.assertEqual(exercise_08(9,10,10), 10, "This should be 10")
        self.assertEqual(exercise_08(0,0,0), 0, "This Should be 0")
        self.assertEqual(exercise_08(-1,2,3), 2, "This Should be 2")
        self.assertEqual(exercise_08(-1,-2,-3), -2, "This Should be -2")
    
    def test_exercise_09(self):
        """
        Test exercise_09 which will return the concat of the first letters of every non-empty string in the list.
        """
        self.assertEqual(exercise_09(['Hi', 'elephants', '', 'like', 'lazy', 'olives']), "Hello", "This should be Hello")
        self.assertEqual(exercise_09(['elephants', '', 'man', 'lazy', 'you', "on", "not"]), "emlyon", "This should be emlyon")
        self.assertEqual(exercise_09([]), "", "This should be empty string")
        self.assertEqual(exercise_09([""]), "", "This should be empty string")
    
    def test_exercise_10(self):
        """
        Test exercise_10 which returns the longest string in the list.
        """
        self.assertEqual(exercise_10(['Hi', 'elephants', '', 'like', 'lazy', 'olives']), "elephants", "This should return elephants")
        with self.assertRaises(ValueError):
            result = exercise_10([])


if __name__ == '__main__':
    unittest.main()