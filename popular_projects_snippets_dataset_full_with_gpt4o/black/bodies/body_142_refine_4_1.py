from collections import namedtuple # pragma: no cover
import token # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'value', 'prefix']) # pragma: no cover
leaf = Leaf(type=token.NAME, value='example_value', prefix='') # pragma: no cover
BRACKETS = {'(', ')', '[', ']', '{', '}'} # pragma: no cover
preformatted = False # pragma: no cover
def whitespace(leaf, complex_subscript): return ' ' # pragma: no cover
track_bracket = False # pragma: no cover
BracketTracker = type('BracketTracker', (object,), {'mark': lambda self, leaf: None}) # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
  'is_class_paren_empty': False, # pragma: no cover
  'leaves': [], # pragma: no cover
  'is_complex_subscript': lambda self, leaf: False, # pragma: no cover
  'inside_brackets': False, # pragma: no cover
  'bracket_tracker': BracketTracker(), # pragma: no cover
  'mode': type('Mode', (object,), {'magic_trailing_comma': False})(), # pragma: no cover
  'has_magic_trailing_comma': lambda self, leaf, ensure_removable=False: False, # pragma: no cover
  'magic_trailing_comma': None, # pragma: no cover
  'remove_trailing_comma': lambda self: None, # pragma: no cover
  'append_comment': lambda self, leaf: False # pragma: no cover
}) # pragma: no cover

from collections import namedtuple # pragma: no cover
import token # pragma: no cover

Leaf = namedtuple('Leaf', ['type', 'value', 'prefix']) # pragma: no cover
leaf = Leaf(type=token.NAME, value='example_value', prefix='') # pragma: no cover
BRACKETS = {'(', ')', '[', ']', '{', '}'} # pragma: no cover
preformatted = False # pragma: no cover
def whitespace(leaf, complex_subscript): return ' ' # pragma: no cover
track_bracket = False # pragma: no cover
BracketTracker = type('BracketTracker', (object,), {'mark': lambda self, leaf: None}) # pragma: no cover

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
