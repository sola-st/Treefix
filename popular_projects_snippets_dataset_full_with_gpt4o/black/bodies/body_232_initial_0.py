def assert_is_leaf_string(s): assert isinstance(s, str), 'Input must be a string' # pragma: no cover
string = 'rfexample_string' # pragma: no cover
STRING_PREFIX_CHARS = set(['r', 'f']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
from l3.Runtime import _l_
"""
    Pre-conditions:
        * assert_is_leaf_string(@string)

    Returns:
        @string's prefix (e.g. '', 'r', 'f', or 'rf').
    """
assert_is_leaf_string(string)
_l_(16481)

prefix = ""
_l_(16482)
prefix_idx = 0
_l_(16483)
while string[prefix_idx] in STRING_PREFIX_CHARS:
    _l_(16486)

    prefix += string[prefix_idx]
    _l_(16484)
    prefix_idx += 1
    _l_(16485)
aux = prefix
_l_(16487)

exit(aux)
