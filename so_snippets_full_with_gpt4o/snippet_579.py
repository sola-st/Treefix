# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe
from l3.Runtime import _l_
try:
    from collections import Counter
    _l_(12996)

except ImportError:
    pass

A = Counter({'a':1, 'b':2, 'c':3})
_l_(12997)
B = Counter({'b':3, 'c':4, 'd':5}) 
_l_(12998) 
C = Counter({'a': 5, 'e':3})
_l_(12999)
list_of_counts = [A, B, C]
_l_(13000)

total = sum(list_of_counts, Counter())
_l_(13001)

print(total)
_l_(13002)
# Counter({'c': 7, 'a': 6, 'b': 5, 'd': 5, 'e': 3})

total = Counter()
_l_(13003)
for count in list_of_counts:
    _l_(13005)

    total += count
    _l_(13004)
print(total)
_l_(13006)
# Counter({'c': 7, 'a': 6, 'b': 5, 'd': 5, 'e': 3})

