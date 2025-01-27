# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
from l3.Runtime import _l_
def maybeMakeNumber(s):
    _l_(2627)

    """Returns a string 's' into a integer if possible, a float if needed or
    returns it as is."""

    # handle None, "", 0
    if not s:
        _l_(2620)

        aux = s
        _l_(2619)
        return aux
    try:
        _l_(2626)

        f = float(s)
        _l_(2621)
        i = int(f)
        _l_(2622)
        aux = i if f == i else f
        _l_(2623)
        return aux
    except ValueError:
        _l_(2625)

        aux = s
        _l_(2624)
        return aux

data = ["unkind", "data", "42", 98, "47.11", "of mixed", "types"]
_l_(2628)

converted = list(map(maybeMakeNumber, data))
_l_(2629)
print(converted)
_l_(2630)

['unkind', 'data', 42, 98, 47.11, 'of mixed', 'types']
_l_(2631)
try:
    from collections.abc import Iterable, Mapping
    _l_(2633)

except ImportError:
    pass

def convertEr(iterab):
    _l_(2640)

    """Tries to convert an iterable to list of floats, ints or the original thing
    from the iterable. Converts any iterable (tuple,set, ...) to itself in output.
    Does not work for Mappings  - you would need to check abc.Mapping and handle 
    things like {1:42, "1":84} when converting them - so they come out as is."""

    if isinstance(iterab, str):
        _l_(2635)

        aux = maybeMakeNumber(iterab)
        _l_(2634)
        return aux

    if isinstance(iterab, Mapping):
        _l_(2637)

        aux = iterab
        _l_(2636)
        return aux

    if isinstance(iterab, Iterable):
        _l_(2639)

        aux = iterab.__class__(convertEr(p) for p in iterab)
        _l_(2638)
        return aux


data = ["unkind", {1: 3,"1":42}, "data", "42", 98, "47.11", "of mixed", 
        ("0", "8", {"15", "things"}, "3.141"), "types"]
_l_(2641)

converted = convertEr(data)
_l_(2642)
print(converted)
_l_(2643)

['unkind', {1: 3, '1': 42}, 'data', 42, 98, 47.11, 'of mixed', 
 (0, 8, {'things', 15}, 3.141), 'types'] # sets are unordered, hence diffrent order
_l_(2644) # sets are unordered, hence diffrent order

