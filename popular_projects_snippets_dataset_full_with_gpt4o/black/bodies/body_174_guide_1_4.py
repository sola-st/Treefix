import token # pragma: no cover

class MockBracketTracker: # pragma: no cover
    def __init__(self, delimiters=None): # pragma: no cover
        self.delimiters = delimiters or [] # pragma: no cover
    def max_delimiter_priority(self): # pragma: no cover
        return 2 # pragma: no cover
    def delimiter_count_with_priority(self, priority): # pragma: no cover
        return 1 # pragma: no cover
 # pragma: no cover
class MockLeaf: # pragma: no cover
    def __init__(self, type, parent=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.parent = parent # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, leaves, delimiters=None): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.bracket_tracker = MockBracketTracker(delimiters) # pragma: no cover
 # pragma: no cover
OPENING_BRACKETS = [token.LPAR, token.LBRACE, token.LSQB] # pragma: no cover
CLOSING_BRACKETS = [token.RPAR, token.RBRACE, token.RSQB] # pragma: no cover
DOT_PRIORITY = 2 # pragma: no cover
line_length = 80 # pragma: no cover
 # pragma: no cover
def _can_omit_opening_paren(line, first, line_length): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def _can_omit_closing_paren(line, last, line_length): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def is_multiline_string(leaf): # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
syms = type('MockSyms', (object,), {'trailer': 100}) # pragma: no cover
 # pragma: no cover
line = MockLine( # pragma: no cover
    leaves=[ # pragma: no cover
        MockLeaf(type=token.LPAR), # pragma: no cover
        MockLeaf(type=token.NAME), # pragma: no cover
        MockLeaf(type=token.RPAR), # pragma: no cover
    ], # pragma: no cover
    delimiters=[('(', 1), (')', 2)] # pragma: no cover
) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Does `line` have a shape safe to reformat without optional parens around it?

    Returns True for only a subset of potentially nice looking formattings but
    the point is to not return false positives that end up producing lines that
    are too long.
    """
bt = line.bracket_tracker
_l_(19599)
if not bt.delimiters:
    _l_(19601)

    aux = True
    _l_(19600)
    # Without delimiters the optional parentheses are useless.
    exit(aux)

max_priority = bt.max_delimiter_priority()
_l_(19602)
if bt.delimiter_count_with_priority(max_priority) > 1:
    _l_(19604)

    aux = False
    _l_(19603)
    # With more than one delimiter of a kind the optional parentheses read better.
    exit(aux)

if max_priority == DOT_PRIORITY:
    _l_(19606)

    aux = True
    _l_(19605)
    # A single stranded method call doesn't require optional parentheses.
    exit(aux)

assert len(line.leaves) >= 2, "Stranded delimiter"
_l_(19607)

# With a single delimiter, omit if the expression starts or ends with
# a bracket.
first = line.leaves[0]
_l_(19608)
second = line.leaves[1]
_l_(19609)
if first.type in OPENING_BRACKETS and second.type not in CLOSING_BRACKETS:
    _l_(19612)

    if _can_omit_opening_paren(line, first=first, line_length=line_length):
        _l_(19611)

        aux = True
        _l_(19610)
        exit(aux)

penultimate = line.leaves[-2]
_l_(19613)
last = line.leaves[-1]
_l_(19614)

if (
    last.type == token.RPAR
    or last.type == token.RBRACE
    or (
        # don't use indexing for omitting optional parentheses;
        # it looks weird
        last.type == token.RSQB
        and last.parent
        and last.parent.type != syms.trailer
    )
):
    _l_(19621)

    if penultimate.type in OPENING_BRACKETS:
        _l_(19616)

        aux = False
        _l_(19615)
        # Empty brackets don't help.
        exit(aux)

    if is_multiline_string(first):
        _l_(19618)

        aux = True
        _l_(19617)
        # Additional wrapping of a multiline string in this situation is
        # unnecessary.
        exit(aux)

    if _can_omit_closing_paren(line, last=last, line_length=line_length):
        _l_(19620)

        aux = True
        _l_(19619)
        exit(aux)
aux = False
_l_(19622)

exit(aux)
