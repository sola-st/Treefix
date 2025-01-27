# Extracted from https://stackoverflow.com/questions/5105517/deep-copy-of-a-dict-in-python
import copy
d = { ... }
d2 = copy.deepcopy(d)

Python 3.2 (r32:88445, Feb 20 2011, 21:30:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
import copy
my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
my_copy = copy.deepcopy(my_dict)
my_dict['a'][2] = 7
my_copy['a'][2]
3


