import token # pragma: no cover
from collections import namedtuple # pragma: no cover
from typing import List, Any # pragma: no cover

BracketTracker = namedtuple('BracketTracker', ['delimiters', 'max_delimiter_priority', 'delimiter_count_with_priority']) # pragma: no cover
OPENING_BRACKETS = {'(', '[', '{'} # pragma: no cover
CLOSING_BRACKETS = {')', ']', '}'} # pragma: no cover
line_length = 10 # pragma: no cover
def is_multiline_string(value): return isinstance(value, str) and '\n' in value # pragma: no cover
def _can_omit_opening_paren(line, first, line_length): return len(line.leaves) < line_length # pragma: no cover
def _can_omit_closing_paren(line, last, line_length): return len(line.leaves) < line_length # pragma: no cover
line = type('MockLine', (object,), {'bracket_tracker': BracketTracker(delimiters=['(', ')'], max_delimiter_priority=lambda: 1, delimiter_count_with_priority=lambda x: 1), 'leaves': [{'type': 'token.RPAR'}, {'type': 'token.RBRACE'}, {'type': 'token.RSQB'}, {'type': 'token.RSQB', 'parent': type('parentMock', (object,), {'type': 'syms.trailer'})}]})() # pragma: no cover
DOT_PRIORITY = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Does `line` have a shape safe to reformat without optional parens around it?

    Returns True for only a subset of potentially nice looking formattings but
    the point is to not return false positives that end up producing lines that
    are too long.
    """
bt = line.bracket_tracker
_l_(7777)
if not bt.delimiters:
    _l_(7779)

    aux = True
    _l_(7778)
    # Without delimiters the optional parentheses are useless.
    exit(aux)

max_priority = bt.max_delimiter_priority()
_l_(7780)
if bt.delimiter_count_with_priority(max_priority) > 1:
    _l_(7782)

    aux = False
    _l_(7781)
    # With more than one delimiter of a kind the optional parentheses read better.
    exit(aux)

if max_priority == DOT_PRIORITY:
    _l_(7784)

    aux = True
    _l_(7783)
    # A single stranded method call doesn't require optional parentheses.
    exit(aux)

assert len(line.leaves) >= 2, "Stranded delimiter"
_l_(7785)

# With a single delimiter, omit if the expression starts or ends with
# a bracket.
first = line.leaves[0]
_l_(7786)
second = line.leaves[1]
_l_(7787)
if first.type in OPENING_BRACKETS and second.type not in CLOSING_BRACKETS:
    _l_(7790)

    if _can_omit_opening_paren(line, first=first, line_length=line_length):
        _l_(7789)

        aux = True
        _l_(7788)
        exit(aux)

penultimate = line.leaves[-2]
_l_(7791)
last = line.leaves[-1]
_l_(7792)

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
    _l_(7799)

    if penultimate.type in OPENING_BRACKETS:
        _l_(7794)

        aux = False
        _l_(7793)
        # Empty brackets don't help.
        exit(aux)

    if is_multiline_string(first):
        _l_(7796)

        aux = True
        _l_(7795)
        # Additional wrapping of a multiline string in this situation is
        # unnecessary.
        exit(aux)

    if _can_omit_closing_paren(line, last=last, line_length=line_length):
        _l_(7798)

        aux = True
        _l_(7797)
        exit(aux)
aux = False
_l_(7800)

exit(aux)
