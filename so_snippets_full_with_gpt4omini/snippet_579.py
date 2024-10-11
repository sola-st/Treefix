# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe
from l3.Runtime import _l_
try:
    from collections import Counter
    _l_(1331)

except ImportError:
    pass

A = Counter({'a':1, 'b':2, 'c':3})
_l_(1332)
B = Counter({'b':3, 'c':4, 'd':5}) 
_l_(1333) 
C = Counter({'a': 5, 'e':3})
_l_(1334)
list_of_counts = [A, B, C]
_l_(1335)

total = sum(list_of_counts, Counter())
_l_(1336)

print(total)
_l_(1337)
# Counter({'c': 7, 'a': 6, 'b': 5, 'd': 5, 'e': 3})

total = Counter()
_l_(1338)
for count in list_of_counts:
    _l_(1340)

    total += count
    _l_(1339)
print(total)
_l_(1341)
# Counter({'c': 7, 'a': 6, 'b': 5, 'd': 5, 'e': 3})

