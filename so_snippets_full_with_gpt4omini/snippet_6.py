# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression
from l3.Runtime import _l_
try:
    from collections import Counter
    _l_(1032)

except ImportError:
    pass
dict1 = {'a':1, 'b': 2}
_l_(1033)
dict2 = {'b':10, 'c': 11}
_l_(1034)
result = dict(Counter(dict1) + Counter(dict2))
_l_(1035)

