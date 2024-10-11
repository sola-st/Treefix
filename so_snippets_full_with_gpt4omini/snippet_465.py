# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-yield-from-syntax-in-python-3-3
from l3.Runtime import _l_
def flatten(sequence):
    _l_(1300)

    """flatten a multi level list or something
    >>> list(flatten([1, [2], 3]))
    [1, 2, 3]
    >>> list(flatten([1, [2], [3, [4]]]))
    [1, 2, 3, 4]
    """
    for element in sequence:
        _l_(1299)

        if hasattr(element, '__iter__'):
            _l_(1298)

            yield from flatten(element)
            _l_(1296)
        else:
            yield element
            _l_(1297)

print(list(flatten([1, [2], [3, [4]]])))
_l_(1301)

