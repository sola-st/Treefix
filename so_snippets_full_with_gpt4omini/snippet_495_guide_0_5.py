# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
from l3.Runtime import _l_
a = ['a', 'b', 'c']
_l_(2949)
str = "a123"
_l_(2950)
if set(a) & set(str):
    _l_(2953)

    print("some of the strings found in str")
    _l_(2951)
else:
    print("no strings found in str")
    _l_(2952)

