# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Assignment \#1 - the Python beginner
# 
# 0) Create a function which computes the area of a rectangle given its height and width. Example: given 10 and 20, should return 200.
# 
# 1) Create a function which given 2 booleans computes the exclusive OR (should return True if one boolean is True and the other boolean is False; and False if both booleans are True or both booleans are False). Example: given True and False, should return True.
# 
# 2) Create a function which given hours, minutes and seconds computes the total number of seconds. Example: given 1 hour, 1 minute and 1 second, should return 3661.
# 
# 3) Create a function which given an integer, compute the sum of all integers between this integer and its double included. Example: given 3, should return 18 (3 + 4 + 5 + 6).
# 
# 4) Create a function which given a string produces a 2 characters string with the first character of the initial string and the last one. If the initial string is empty, it should return an empty string. Example: given 'Python', should return 'Pn'.
# 
# 5) Create a function which given a string returns the sentence: 'The reverse of X is Y!' where X is the initial string and Y is the reverse of the initial string. Example: given 'Paris', should return 'The reverse of Paris is siraP!'.
# 
# 6) Create a function which given a string returns True if the letters of the string are unique and False otherwise. Example: given 'Python', should return True; and given 'alphabet', should return False.
# 
# 7) Create a function which given a string returns True if the string is a palindrome (e.g., a word which has the property of reading the same forwards as it does backwards) and False otherwise. Example, given 'tattarrattat', should return True; and given 'alphabet', should return False.
# 
# 8) Create a function which given 3 numbers returns the one which is in the middle. Example: given 9, 5 and 6, should return 6.
# 
# 9) Create a function which given a list of strings produces a string with the first character of each non empty string of the list. Example: given ['Hi', 'elephants', '', 'like', 'lazy', 'olives'], should return 'Hello'.
# 
# 10) Create a function which given a list of strings returns the longest one. Example: given ['Hi', 'elephants', '', 'like', 'lazy', 'olives'], should return 'elephants'.

# %%
# THIS IS AN EXAMPLE. THERE IS NOTHING TO DO. IT WILL NOT BE GRADED.
# 0) Create a function which computes the area of a rectangle given its height and width.
def exercise_00(height, width):
    result = height * width
    return result


# %%
# run and check
exercise_00(10, 20)


# %%
# 1) Create a function which given 2 booleans computes the exclusive OR.
# (should return True if one boolean is True and the other boolean is false, False if both booleans are True or both booleans are False).
def exercise_01(bool1, bool2):
    # change the line 'result = None' to perform the appropriate calculation
    result = bool1 ^ bool2
    return result


# %%
# run and check
exercise_01(True, False)


# %%
# 2) Create a function which given hours, minutes and seconds computes the total of seconds.
def exercise_02(hours, minutes, seconds):
    # change the line 'result = None' to perform the appropriate calculation
    result = sum([hours*60*60, minutes*60, seconds])
    return result


# %%
# run and check
exercise_02(1, 1, 1)


# %%
# 3) Create a function which given an integer, compute the sum of all integers between this integer and its double included.
def exercise_03(integer):
    # change the line 'result = None' to perform the appropriate calculation
    result = sum(range(integer, integer * 2 +1))
    return result


# %%
# run and check
exercise_03(3)


# %%
# 4) Create a function which given a string produces a 2 characters string with the first character of the initial string and the last one.
# If the initial string is empty, it should return an empty string.
def exercise_04(string):
    # change the line 'result = None' to perform the appropriate calculation
    if string: result = string[0] + string[-1]
    else: result = string
    return result


# %%
# run and check
exercise_04('Python')


# %%
# 5) Create a function which given a string returns the sentence: 'The reverse of X is Y!'
def exercise_05(string):
    # change the line 'result = None' to perform the appropriate calculation
    result = f"The reverse of {string} is {string[::-1]}!"
    return result


# %%
# run and check
exercise_05('Paris')


# %%
# 6) Create a function which given a string returns True if the letters of the string are unique and False otherwise.
def exercise_06(string):
    # change the line 'result = None' to perform the appropriate calculation
    result = len(string) == len(set(string))
    return result


# %%
# run and check
exercise_06('Python')


# %%
# 7) Create a function which given a string returns True if the string is a palindrome
# (e.g., a word which has the property of reading the same forwards as it does backwards) and False otherwise.
def exercise_07(string):
    # change the line 'result = None' to perform the appropriate calculation
    result = string == string[::-1]
    return result


# %%
# run and check
exercise_07('tattarrattat')


# %%
# 8) Create a function which given 3 numbers returns the one which is in the middle.
def exercise_08(number1, number2, number3):
    # change the line 'result = None' to perform the appropriate calculation
    result = sorted([number1, number2, number3])
    return result[1]


# %%
# run and check
exercise_08(9, 5, 6)


# %%
# 9) Create a function which given a list of strings produces a string with the first character of each non empty string of the list.
def exercise_09(list_of_strings):
    # change the line 'result = None' to perform the appropriate calculation
    result = "".join([s[0] for s in list_of_strings if len(s) != 0])
    return result


# %%
# run and check
exercise_09(['Hi', 'elephants', '', 'like', 'lazy', 'olives'])


# %%
# 10) Create a function which given a list of strings returns the longest one.
def exercise_10(list_of_strings):
    # change the line 'result = None' to perform the appropriate calculation
    result = max(list_of_strings, key=len)
    return result


# %%
# run and check
exercise_10(['Hi', 'elephants', '', 'like', 'lazy', 'olives'])


