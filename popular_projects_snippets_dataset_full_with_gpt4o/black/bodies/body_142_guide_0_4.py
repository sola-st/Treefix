from typing import List, Any # pragma: no cover
from types import SimpleNamespace # pragma: no cover

leaf = SimpleNamespace(type='COLON', value=':') # pragma: no cover
BRACKETS = {'PAREN', 'BRACE'} # pragma: no cover
preformatted = False # pragma: no cover
self = SimpleNamespace( # pragma: no cover
    is_class_paren_empty=True, # pragma: no cover
    leaves=[SimpleNamespace(prefix='')], # pragma: no cover
    inside_brackets=True, # pragma: no cover
    bracket_tracker=type('Mock', (object,), {'mark': lambda self, leaf: None})(), # pragma: no cover
    mode=SimpleNamespace(magic_trailing_comma=True), # pragma: no cover
    has_magic_trailing_comma=lambda leaf, ensure_removable=False: False, # pragma: no cover
    append_comment=lambda leaf: False # pragma: no cover
) # pragma: no cover
def whitespace(leaf, complex_subscript): # pragma: no cover
    return ' ' # pragma: no cover
self.remove_trailing_comma = lambda: None # pragma: no cover

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
