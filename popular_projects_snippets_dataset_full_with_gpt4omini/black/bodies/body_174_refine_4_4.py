from typing import List, Callable # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.delimiters = []# pragma: no cover
    def max_delimiter_priority(self):# pragma: no cover
        return DOT_PRIORITY# pragma: no cover
    def delimiter_count_with_priority(self, priority):# pragma: no cover
        return 1# pragma: no cover
# pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = MockBracketTracker()# pragma: no cover
        self.leaves = [MockToken('(', 'OPENING_BRACKET'), MockToken('a', 'IDENTIFIER'), MockToken(')', 'CLOSING_BRACKET')]# pragma: no cover
# pragma: no cover
class MockToken:# pragma: no cover
    def __init__(self, type, name):# pragma: no cover
        self.type = type# pragma: no cover
        self.name = name# pragma: no cover
        self.parent = None# pragma: no cover
# pragma: no cover
line = MockLine()# pragma: no cover
DOT_PRIORITY = 1# pragma: no cover
OPENING_BRACKETS = ['(']# pragma: no cover
CLOSING_BRACKETS = [')']# pragma: no cover
line_length = 50# pragma: no cover
# pragma: no cover
def _can_omit_opening_paren(line, first, line_length):# pragma: no cover
    return False# pragma: no cover
# pragma: no cover
def _can_omit_closing_paren(line, last, line_length):# pragma: no cover
    return True# pragma: no cover
# pragma: no cover
def is_multiline_string(first):# pragma: no cover
    return False# pragma: no cover
# pragma: no cover
token = type('MockTokenModule', (object,), {'RPAR': ')', 'RBRACE': '}', 'RSQB': ']'})# pragma: no cover
syms = type('MockSymbols', (object,), {'trailer': 'trailer'}) # pragma: no cover

from typing import List, Callable, Any # pragma: no cover

class MockBracketTracker:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.delimiters = ['+', '-', '*', '/']# pragma: no cover
    def max_delimiter_priority(self):# pragma: no cover
        return 1# pragma: no cover
    def delimiter_count_with_priority(self, priority):# pragma: no cover
        return 1# pragma: no cover
# pragma: no cover
class MockToken:# pragma: no cover
    def __init__(self, type_name):# pragma: no cover
        self.type = type_name# pragma: no cover
        self.parent = None# pragma: no cover
# pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = MockBracketTracker()# pragma: no cover
        self.leaves = [MockToken('('), MockToken('a'), MockToken(')')]# pragma: no cover
# pragma: no cover
line = MockLine()# pragma: no cover
DOT_PRIORITY = 1# pragma: no cover
OPENING_BRACKETS = ['(', '{', '[']# pragma: no cover
CLOSING_BRACKETS = [')', '}', ']']# pragma: no cover
line_length = 50# pragma: no cover
# pragma: no cover
def _can_omit_opening_paren(line, first, line_length):# pragma: no cover
    return first.type in OPENING_BRACKETS# pragma: no cover
# pragma: no cover
def _can_omit_closing_paren(line, last, line_length):# pragma: no cover
    return last.type in CLOSING_BRACKETS# pragma: no cover
# pragma: no cover
def is_multiline_string(value):# pragma: no cover
    return False# pragma: no cover
# pragma: no cover
token = type('MockTokenModule', (object,), {'RPAR': ')', 'RBRACE': '}', 'RSQB': ']'})# pragma: no cover
syms = type('MockSymbols', (object,), {'trailer': 'trailer'}) # pragma: no cover

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
