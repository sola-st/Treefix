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
_l_(4886)

prefix = ""
_l_(4887)
prefix_idx = 0
_l_(4888)
while string[prefix_idx] in STRING_PREFIX_CHARS:
    _l_(4891)

    prefix += string[prefix_idx]
    _l_(4889)
    prefix_idx += 1
    _l_(4890)
aux = prefix
_l_(4892)

exit(aux)
