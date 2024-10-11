# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5384914/how-do-i-delete-items-from-a-dictionary-while-iterating-over-it
from l3.Runtime import _l_
dict = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4}
_l_(580)
delete = []
_l_(581)
for k,v in dict.items():
    _l_(584)

    if v%2 == 1:
        _l_(583)

        delete.append(k)
        _l_(582)
for i in delete:
    _l_(586)

    del dict[i]
    _l_(585)

