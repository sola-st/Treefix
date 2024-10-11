from typing import List, Optional # pragma: no cover
from dataclasses import dataclass # pragma: no cover

leaf = type('MockLeaf', (), {'type': 'COLON', 'value': 'some_value', 'prefix': ''})() # pragma: no cover
BRACKETS = ['COLON', 'COMMA'] # pragma: no cover
class MockToken: COLON = 'COLON' # pragma: no cover
token = MockToken() # pragma: no cover

from typing import List, Callable # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def mark(self, leaf): pass # pragma: no cover
# pragma: no cover
class MockMode:# pragma: no cover
    magic_trailing_comma = True # pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    leaves: List = []# pragma: no cover
    is_class_paren_empty: bool = True# pragma: no cover
    inside_brackets: bool = False# pragma: no cover
    bracket_tracker = MockBracketTracker()# pragma: no cover
    mode = MockMode()# pragma: no cover
    def has_magic_trailing_comma(self, leaf, ensure_removable=False): return False# pragma: no cover
    def remove_trailing_comma(self): pass# pragma: no cover
    def append_comment(self, leaf): return False# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover
# pragma: no cover
class MockLeaf:# pragma: no cover
    def __init__(self, type: str, value: str, prefix: str):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
        self.prefix = prefix# pragma: no cover
# pragma: no cover
leaf = MockLeaf(type='COLON', value='some_value', prefix='') # pragma: no cover
# pragma: no cover
class MockToken:# pragma: no cover
    COLON = 'COLON'# pragma: no cover
token = MockToken() # pragma: no cover
# pragma: no cover
BRACKETS = ['COLON', 'COMMA'] # pragma: no cover
# pragma: no cover
preformatted = False # pragma: no cover
# pragma: no cover
whitespace = lambda leaf, complex_subscript: '    ' # pragma: no cover
# pragma: no cover
track_bracket = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Add a new `leaf` to the end of the line.

        Unless `preformatted` is True, the `leaf` will receive a new consistent
        whitespace prefix and metadata applied by :class:`BracketTracker`.
        Trailing commas are maybe removed, unpacked for loop variables are
        demoted from being delimiters.

        Inline comments are put aside.
        """
has_value = leaf.type in BRACKETS or bool(leaf.value.strip())
_l_(6948)
if not has_value:
    _l_(6950)

    exit()
    _l_(6949)

if token.COLON == leaf.type and self.is_class_paren_empty:
    _l_(6952)

    del self.leaves[-2:]
    _l_(6951)
if self.leaves and not preformatted:
    _l_(6954)

    # Note: at this point leaf.prefix should be empty except for
    # imports, for which we only preserve newlines.
    leaf.prefix += whitespace(
        leaf, complex_subscript=self.is_complex_subscript(leaf)
    )
    _l_(6953)
if self.inside_brackets or not preformatted or track_bracket:
    _l_(6961)

    self.bracket_tracker.mark(leaf)
    _l_(6955)
    if self.mode.magic_trailing_comma:
        _l_(6960)

        if self.has_magic_trailing_comma(leaf):
            _l_(6957)

            self.magic_trailing_comma = leaf
            _l_(6956)
    elif self.has_magic_trailing_comma(leaf, ensure_removable=True):
        _l_(6959)

        self.remove_trailing_comma()
        _l_(6958)
if not self.append_comment(leaf):
    _l_(6963)

    self.leaves.append(leaf)
    _l_(6962)
