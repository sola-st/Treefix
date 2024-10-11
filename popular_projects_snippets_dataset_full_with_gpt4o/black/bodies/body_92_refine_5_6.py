from typing import Tuple # pragma: no cover

self = type('Mock', (object,), {'__class__': type('MockClass', (object,), {})})() # pragma: no cover

string = r'This is an example with \N{VALID_NAME} expression.' # pragma: no cover
self = type('MockClass', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Yields:
            All ranges of @string which, if @string were to be split there,
            would result in the splitting of an \\N{...} expression (which is NOT
            allowed).
        """
# True - the previous backslash was unescaped
# False - the previous backslash was escaped *or* there was no backslash
previous_was_unescaped_backslash = False
_l_(15826)
it = iter(enumerate(string))
_l_(15827)
for idx, c in it:
    _l_(15842)

    if c == "\\":
        _l_(15830)

        previous_was_unescaped_backslash = not previous_was_unescaped_backslash
        _l_(15828)
        continue
        _l_(15829)
    if not previous_was_unescaped_backslash or c != "N":
        _l_(15833)

        previous_was_unescaped_backslash = False
        _l_(15831)
        continue
        _l_(15832)
    previous_was_unescaped_backslash = False
    _l_(15834)

    begin = idx - 1  # the position of backslash before \N{...}
    _l_(15835)  # the position of backslash before \N{...}
    for idx, c in it:
        _l_(15840)

        if c == "}":
            _l_(15838)

            end = idx
            _l_(15836)
            break
            _l_(15837)
    else:
        # malformed nameescape expression?
        # should have been detected by AST parsing earlier...
        raise RuntimeError(f"{self.__class__.__name__} LOGIC ERROR!")
        _l_(15839)
    aux = (begin, end)
    _l_(15841)
    exit(aux)
