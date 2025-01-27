# Extracted from https://stackoverflow.com/questions/577234/python-extend-for-a-dictionary
d1 = {'a': 1}
d2 = {'b': 2}

extended_dict = d1 | d2
>> {'a':1, 'b': 2}

d1 = {'b': 1}
d2 = {'b': 2}
d1 | d2 
>> {'b': 2} 

