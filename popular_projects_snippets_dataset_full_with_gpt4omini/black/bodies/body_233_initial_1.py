string = "<prefix>sample_string'" # pragma: no cover
STRING_PREFIX_CHARS = '<prefix>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
from l3.Runtime import _l_
"""
    Checks the pre-condition that @string has the format that you would expect
    of `leaf.value` where `leaf` is some Leaf such that `leaf.type ==
    token.STRING`. A more precise description of the pre-conditions that are
    checked are listed below.

    Pre-conditions:
        * @string starts with either ', ", <prefix>', or <prefix>" where
        `set(<prefix>)` is some subset of `set(STRING_PREFIX_CHARS)`.
        * @string ends with a quote character (' or ").

    Raises:
        AssertionError(...) if the pre-conditions listed above are not
        satisfied.
    """
dquote_idx = string.find('"')
_l_(6926)
squote_idx = string.find("'")
_l_(6927)
if -1 in [dquote_idx, squote_idx]:
    _l_(6930)

    quote_idx = max(dquote_idx, squote_idx)
    _l_(6928)
else:
    quote_idx = min(squote_idx, dquote_idx)
    _l_(6929)

assert (
    0 <= quote_idx < len(string) - 1
), f"{string!r} is missing a starting quote character (' or \")."
_l_(6931)
assert string[-1] in (
    "'",
    '"',
), f"{string!r} is missing an ending quote character (' or \")."
_l_(6932)
assert set(string[:quote_idx]).issubset(
    set(STRING_PREFIX_CHARS)
), f"{set(string[:quote_idx])} is NOT a subset of {set(STRING_PREFIX_CHARS)}."
_l_(6933)
