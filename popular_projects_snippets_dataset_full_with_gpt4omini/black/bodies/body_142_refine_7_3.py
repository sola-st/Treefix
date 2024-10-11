from typing import List # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
        self.prefix = '' # pragma: no cover
leaf = MockLeaf(type='some_type', value='some_value') # pragma: no cover
BRACKETS = ['some_type'] # pragma: no cover
class MockToken:# pragma: no cover
    COLON = 'COLON' # pragma: no cover
token = MockToken() # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = []# pragma: no cover
        self.is_class_paren_empty = False# pragma: no cover
        self.inside_brackets = False# pragma: no cover
        self.bracket_tracker = None# pragma: no cover
        self.magic_trailing_comma = None# pragma: no cover
    def is_complex_subscript(self, leaf):# pragma: no cover
        return False# pragma: no cover
    def has_magic_trailing_comma(self, leaf, ensure_removable=False):# pragma: no cover
        return False# pragma: no cover
    def remove_trailing_comma(self):# pragma: no cover
        pass# pragma: no cover
    def append_comment(self, leaf):# pragma: no cover
        return False # pragma: no cover
self = Mock() # pragma: no cover
def whitespace(leaf, complex_subscript):# pragma: no cover
    return ' ' # pragma: no cover
preformatted = False # pragma: no cover
track_bracket = False # pragma: no cover
class MockMode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.magic_trailing_comma = False # pragma: no cover

from typing import List # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
        self.prefix = '' # pragma: no cover
leaf = MockLeaf(type='COLON', value='some_value') # pragma: no cover
BRACKETS = ['COLON'] # pragma: no cover
class MockToken:# pragma: no cover
    COLON = 'COLON' # pragma: no cover
token = MockToken() # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def mark(self, leaf):# pragma: no cover
        print('Marked:', leaf)# pragma: no cover
 # pragma: no cover
class MockMode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.magic_trailing_comma = False # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = []# pragma: no cover
        self.is_class_paren_empty = False# pragma: no cover
        self.inside_brackets = False# pragma: no cover
        self.bracket_tracker = MockBracketTracker()# pragma: no cover
        self.mode = MockMode()# pragma: no cover
        self.magic_trailing_comma = None# pragma: no cover
    def is_complex_subscript(self, leaf):# pragma: no cover
        return False# pragma: no cover
    def has_magic_trailing_comma(self, leaf, ensure_removable=False):# pragma: no cover
        return False# pragma: no cover
    def remove_trailing_comma(self):# pragma: no cover
        pass# pragma: no cover
    def append_comment(self, leaf):# pragma: no cover
        return False # pragma: no cover
self = Mock() # pragma: no cover
def whitespace(leaf, complex_subscript):# pragma: no cover
    return ' ' # pragma: no cover
preformatted = False # pragma: no cover
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
