import token # pragma: no cover

line = type('Mock', (object,), {'bracket_tracker': type('Mock', (object,), {'delimiters': [], 'max_delimiter_priority': lambda: 1, 'delimiter_count_with_priority': lambda priority: 1})(), 'leaves': [type('Mock', (object,), {'type': 1, 'parent': None})(), type('Mock', (object,), {'type': 2, 'parent': None})()]})() # pragma: no cover
DOT_PRIORITY = 2 # pragma: no cover
OPENING_BRACKETS = {1} # pragma: no cover
CLOSING_BRACKETS = {2} # pragma: no cover
_can_omit_opening_paren = lambda line, first, line_length: True # pragma: no cover
line_length = 80 # pragma: no cover
token.RPAR = 3 # pragma: no cover
token.RBRACE = 4 # pragma: no cover
token.RSQB = 5 # pragma: no cover
syms = type('Mock', (object,), {'trailer': 6})() # pragma: no cover
is_multiline_string = lambda leaf: False # pragma: no cover
_can_omit_closing_paren = lambda line, last, line_length: True # pragma: no cover

import token # pragma: no cover

line = type('Mock', (object,), {'bracket_tracker': type('MockTracker', (object,), {'delimiters': [], 'max_delimiter_priority': lambda: 1, 'delimiter_count_with_priority': lambda priority: 1})(), 'leaves': [type('MockLeaf', (object,), {'type': token.LPAR, 'parent': None})(), type('MockLeaf2', (object,), {'type': token.RPAR, 'parent': None})(), type('MockLeaf3', (object,), {'type': token.RPAR, 'parent': None})()]})() # pragma: no cover
DOT_PRIORITY = 2 # pragma: no cover
OPENING_BRACKETS = {token.LPAR, token.LBRACE, token.LSQB} # pragma: no cover
CLOSING_BRACKETS = {token.RPAR, token.RBRACE, token.RSQB} # pragma: no cover
_can_omit_opening_paren = lambda line, first, line_length: True # pragma: no cover
line_length = 80 # pragma: no cover
token.LPAR = 7 # pragma: no cover
token.RPAR = 3 # pragma: no cover
token.RBRACE = 4 # pragma: no cover
token.RSQB = 5 # pragma: no cover
syms = type('MockSyms', (object,), {'trailer': 6})() # pragma: no cover
is_multiline_string = lambda leaf: False # pragma: no cover
_can_omit_closing_paren = lambda line, last, line_length: True # pragma: no cover

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
