# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
from l3.Runtime import _l_
def combinations(arr, carry):
    _l_(12449)

    for i in range(len(arr)):
        _l_(12448)

        yield carry + arr[i]
        _l_(12446)
        yield from combinations(arr[i + 1:], carry + arr[i])
        _l_(12447)

