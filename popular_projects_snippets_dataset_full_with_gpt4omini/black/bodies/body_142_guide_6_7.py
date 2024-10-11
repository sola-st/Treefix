from typing import List, Callable # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, leaf_type: str, value: str): # pragma: no cover
        self.type = leaf_type # pragma: no cover
        self.value = value # pragma: no cover
        self.prefix = '' # pragma: no cover
 # pragma: no cover
class BracketTracker: # pragma: no cover
    def mark(self, leaf): pass # pragma: no cover
 # pragma: no cover
class Mode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.magic_trailing_comma = False # pragma: no cover
 # pragma: no cover
class SelfMock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [] # pragma: no cover
        self.is_class_paren_empty = True # pragma: no cover
  # Set to True to hit line 7 # pragma: no cover
        self.inside_brackets = False # pragma: no cover
        self.bracket_tracker = BracketTracker() # pragma: no cover
        self.mode = Mode() # pragma: no cover
        self.has_magic_trailing_comma = lambda leaf, ensure_removable=False: False # pragma: no cover
        self.remove_trailing_comma = lambda: None # pragma: no cover
        self.append_comment = lambda leaf: False # pragma: no cover
        self.is_complex_subscript = lambda leaf: False # pragma: no cover
 # pragma: no cover
leaf = Leaf('COLON', 'some value') # pragma: no cover
  # Ensure has_value is True # pragma: no cover
self = SelfMock() # pragma: no cover
BRACKETS = ['COLON'] # pragma: no cover
token = type('Token', (), {'COLON': 'COLON'})() # pragma: no cover
preformatted = False # pragma: no cover
  # This should activate lines 6 and following # pragma: no cover
track_bracket = False # pragma: no cover
whitespace = lambda leaf, complex_subscript: '    '  # Function to provide whitespace # pragma: no cover

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
