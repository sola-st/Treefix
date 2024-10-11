import sys # pragma: no cover
from typing import Iterator # pragma: no cover
import token # pragma: no cover
import enum # pragma: no cover

class CannotSplit(Exception): pass # pragma: no cover
class Feature(enum.Enum): TRAILING_COMMA_IN_DEF = 1; TRAILING_COMMA_IN_CALL = 2 # pragma: no cover
class TokenType(enum.Enum): COMMA = 44; STANDALONE_COMMENT = 99 # pragma: no cover
token = TokenType # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover
DOT_PRIORITY = 2 # pragma: no cover
syms = type('syms', (object,), {'typedargslist': 1, 'arglist': 2, 'argument': 3}) # pragma: no cover
def is_vararg(leaf, within): return True # mock implementation # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, type_, value):# pragma: no cover
        self.type = type_# pragma: no cover
        self.value = value# pragma: no cover
        self.bracket_depth = 0# pragma: no cover
# pragma: no cover
class BracketTracker:# pragma: no cover
    def max_delimiter_priority(self, exclude): return 1# pragma: no cover
    def delimiter_count_with_priority(self, priority): return 2# pragma: no cover
    def delimiters(self): return {1: COMMA_PRIORITY}# pragma: no cover
# pragma: no cover
class Line:# pragma: no cover
    def __init__(self, mode=None, depth=0, inside_brackets=False):# pragma: no cover
        self.mode = mode# pragma: no cover
        self.depth = depth# pragma: no cover
        self.inside_brackets = inside_brackets# pragma: no cover
        self.leaves = [Leaf(token.COMMA, ','), Leaf(token.COMMA, ',')]# pragma: no cover
    def append_safe(self, leaf, preformatted=False): pass# pragma: no cover
    def append(self, leaf): pass# pragma: no cover
    def comments_after(self, leaf): return []# pragma: no cover
# pragma: no cover
line = Line()# pragma: no cover
line.bracket_tracker = BracketTracker()# pragma: no cover
features = {Feature.TRAILING_COMMA_IN_DEF, Feature.TRAILING_COMMA_IN_CALL} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Split according to delimiters of the highest priority.

    If the appropriate Features are given, the split will add trailing commas
    also in function signatures and calls that contain `*` and `**`.
    """
try:
    _l_(18145)

    last_leaf = line.leaves[-1]
    _l_(18142)
except IndexError:
    _l_(18144)

    raise CannotSplit("Line empty") from None
    _l_(18143)

bt = line.bracket_tracker
_l_(18146)
try:
    _l_(18150)

    delimiter_priority = bt.max_delimiter_priority(exclude={id(last_leaf)})
    _l_(18147)
except ValueError:
    _l_(18149)

    raise CannotSplit("No delimiters found") from None
    _l_(18148)

if delimiter_priority == DOT_PRIORITY:
    _l_(18153)

    if bt.delimiter_count_with_priority(delimiter_priority) == 1:
        _l_(18152)

        raise CannotSplit("Splitting a single attribute from its owner looks wrong")
        _l_(18151)

current_line = Line(
    mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
)
_l_(18154)
lowest_depth = sys.maxsize
_l_(18155)
trailing_comma_safe = True
_l_(18156)

def append_to_line(leaf: Leaf) -> Iterator[Line]:
    _l_(18164)

    """Append `leaf` to current line or to new line if appending impossible."""
    nonlocal current_line
    _l_(18157)
    try:
        _l_(18163)

        current_line.append_safe(leaf, preformatted=True)
        _l_(18158)
    except ValueError:
        _l_(18162)

        aux = current_line
        _l_(18159)
        exit(aux)

        current_line = Line(
            mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
        _l_(18160)
        current_line.append(leaf)
        _l_(18161)

for leaf in line.leaves:
    _l_(18178)

    aux = append_to_line(leaf)
    _l_(18165)
    exit(aux)

    for comment_after in line.comments_after(leaf):
        _l_(18167)

        aux = append_to_line(comment_after)
        _l_(18166)
        exit(aux)

    lowest_depth = min(lowest_depth, leaf.bracket_depth)
    _l_(18168)
    if leaf.bracket_depth == lowest_depth:
        _l_(18173)

        if is_vararg(leaf, within={syms.typedargslist}):
            _l_(18172)

            trailing_comma_safe = (
                trailing_comma_safe and Feature.TRAILING_COMMA_IN_DEF in features
            )
            _l_(18169)
        elif is_vararg(leaf, within={syms.arglist, syms.argument}):
            _l_(18171)

            trailing_comma_safe = (
                trailing_comma_safe and Feature.TRAILING_COMMA_IN_CALL in features
            )
            _l_(18170)

    leaf_priority = bt.delimiters.get(id(leaf))
    _l_(18174)
    if leaf_priority == delimiter_priority:
        _l_(18177)

        aux = current_line
        _l_(18175)
        exit(aux)

        current_line = Line(
            mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
        _l_(18176)
if current_line:
    _l_(18183)

    if (
        trailing_comma_safe
        and delimiter_priority == COMMA_PRIORITY
        and current_line.leaves[-1].type != token.COMMA
        and current_line.leaves[-1].type != STANDALONE_COMMENT
    ):
        _l_(18181)

        new_comma = Leaf(token.COMMA, ",")
        _l_(18179)
        current_line.append(new_comma)
        _l_(18180)
    aux = current_line
    _l_(18182)
    exit(aux)
