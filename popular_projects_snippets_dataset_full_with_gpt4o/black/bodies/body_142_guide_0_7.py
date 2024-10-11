from typing import List # pragma: no cover
import token # pragma: no cover

class BracketTracker: # pragma: no cover
    def mark(self, leaf): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class Mode: # pragma: no cover
    magic_trailing_comma = False # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.type = token.COMMA # pragma: no cover
        self.value = ' ' # pragma: no cover
        self.prefix = '' # pragma: no cover
 # pragma: no cover
class ComplexSubscriptTracker: # pragma: no cover
    def __init__(self, leaf): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
def whitespace(leaf, complex_subscript): # pragma: no cover
    return ' ' # pragma: no cover
 # pragma: no cover
leaf = Mock() # pragma: no cover
self = type('Mock', (object,), dict( # pragma: no cover
    leaves=[Mock()], # pragma: no cover
    inside_brackets=False, # pragma: no cover
    is_class_paren_empty=False, # pragma: no cover
    bracket_tracker=BracketTracker(), # pragma: no cover
    mode=Mode(), # pragma: no cover
    has_magic_trailing_comma=lambda leaf: False, # pragma: no cover
    remove_trailing_comma=lambda: None, # pragma: no cover
    append_comment=lambda leaf: False, # pragma: no cover
    is_complex_subscript=lambda leaf: ComplexSubscriptTracker(leaf) # pragma: no cover
)) # pragma: no cover

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
_l_(18439)
if not has_value:
    _l_(18441)

    exit()
    _l_(18440)

if token.COLON == leaf.type and self.is_class_paren_empty:
    _l_(18443)

    del self.leaves[-2:]
    _l_(18442)
if self.leaves and not preformatted:
    _l_(18445)

    # Note: at this point leaf.prefix should be empty except for
    # imports, for which we only preserve newlines.
    leaf.prefix += whitespace(
        leaf, complex_subscript=self.is_complex_subscript(leaf)
    )
    _l_(18444)
if self.inside_brackets or not preformatted or track_bracket:
    _l_(18452)

    self.bracket_tracker.mark(leaf)
    _l_(18446)
    if self.mode.magic_trailing_comma:
        _l_(18451)

        if self.has_magic_trailing_comma(leaf):
            _l_(18448)

            self.magic_trailing_comma = leaf
            _l_(18447)
    elif self.has_magic_trailing_comma(leaf, ensure_removable=True):
        _l_(18450)

        self.remove_trailing_comma()
        _l_(18449)
if not self.append_comment(leaf):
    _l_(18454)

    self.leaves.append(leaf)
    _l_(18453)
