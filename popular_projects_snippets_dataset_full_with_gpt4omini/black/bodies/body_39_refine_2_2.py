from typing import Iterator # pragma: no cover
import sys # pragma: no cover
import token # pragma: no cover

class CannotSplit(Exception): pass # pragma: no cover
class MockLeaf: # pragma: no cover
    def __init__(self, bracket_depth, leaf_type): # pragma: no cover
        self.bracket_depth = bracket_depth # pragma: no cover
        self.type = leaf_type # pragma: no cover
# pragma: no cover
class MockBracketTracker: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.delimiters = {id(leaf): 1 for leaf in leaves} # pragma: no cover
    # pragma: no cover
    def max_delimiter_priority(self, exclude=set()): # pragma: no cover
        return 1 # pragma: no cover
# pragma: no cover
    def delimiter_count_with_priority(self, priority): # pragma: no cover
        return 1 # pragma: no cover
    # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, mode, depth, inside_brackets, leaves, comments_after): # pragma: no cover
        self.mode = mode # pragma: no cover
        self.depth = depth # pragma: no cover
        self.inside_brackets = inside_brackets # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.bracket_tracker = MockBracketTracker(leaves) # pragma: no cover
        self.comments_after = comments_after # pragma: no cover
    # pragma: no cover
    def append_safe(self, leaf, preformatted=False): # pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
    # pragma: no cover
class Feature: # pragma: no cover
    TRAILING_COMMA_IN_DEF = 'trailing_comma_in_def' # pragma: no cover
    TRAILING_COMMA_IN_CALL = 'trailing_comma_in_call' # pragma: no cover
# pragma: no cover
class MockToken: # pragma: no cover
    COMMA = 1# pragma: no cover
    STANDALONE_COMMENT = 2# pragma: no cover
# pragma: no cover
line = MockLine(# pragma: no cover
    mode='test', # pragma: no cover
    depth=0, # pragma: no cover
    inside_brackets=False, # pragma: no cover
    leaves=[MockLeaf(bracket_depth=0, leaf_type=1)], # pragma: no cover
    comments_after=lambda leaf: [] # pragma: no cover
)# pragma: no cover
# pragma: no cover
DOT_PRIORITY = 1# pragma: no cover
COMMA_PRIORITY = 2# pragma: no cover
features = {Feature.TRAILING_COMMA_IN_DEF, Feature.TRAILING_COMMA_IN_CALL}# pragma: no cover
syms = type('MockSyms', (), {'typedargslist': 1, 'arglist': 1, 'argument': 1})# pragma: no cover
Leaf = MockLeaf# pragma: no cover
token = MockToken# pragma: no cover
 # pragma: no cover

from typing import Iterator # pragma: no cover
import sys # pragma: no cover
import token # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Split according to delimiters of the highest priority.

    If the appropriate Features are given, the split will add trailing commas
    also in function signatures and calls that contain `*` and `**`.
    """
try:
    _l_(6382)

    last_leaf = line.leaves[-1]
    _l_(6379)
except IndexError:
    _l_(6381)

    raise CannotSplit("Line empty") from None
    _l_(6380)

bt = line.bracket_tracker
_l_(6383)
try:
    _l_(6387)

    delimiter_priority = bt.max_delimiter_priority(exclude={id(last_leaf)})
    _l_(6384)
except ValueError:
    _l_(6386)

    raise CannotSplit("No delimiters found") from None
    _l_(6385)

if delimiter_priority == DOT_PRIORITY:
    _l_(6390)

    if bt.delimiter_count_with_priority(delimiter_priority) == 1:
        _l_(6389)

        raise CannotSplit("Splitting a single attribute from its owner looks wrong")
        _l_(6388)

current_line = Line(
    mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
)
_l_(6391)
lowest_depth = sys.maxsize
_l_(6392)
trailing_comma_safe = True
_l_(6393)

def append_to_line(leaf: Leaf) -> Iterator[Line]:
    _l_(6401)

    """Append `leaf` to current line or to new line if appending impossible."""
    nonlocal current_line
    _l_(6394)
    try:
        _l_(6400)

        current_line.append_safe(leaf, preformatted=True)
        _l_(6395)
    except ValueError:
        _l_(6399)

        aux = current_line
        _l_(6396)
        exit(aux)

        current_line = Line(
            mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
        _l_(6397)
        current_line.append(leaf)
        _l_(6398)

for leaf in line.leaves:
    _l_(6415)

    aux = append_to_line(leaf)
    _l_(6402)
    exit(aux)

    for comment_after in line.comments_after(leaf):
        _l_(6404)

        aux = append_to_line(comment_after)
        _l_(6403)
        exit(aux)

    lowest_depth = min(lowest_depth, leaf.bracket_depth)
    _l_(6405)
    if leaf.bracket_depth == lowest_depth:
        _l_(6410)

        if is_vararg(leaf, within={syms.typedargslist}):
            _l_(6409)

            trailing_comma_safe = (
                trailing_comma_safe and Feature.TRAILING_COMMA_IN_DEF in features
            )
            _l_(6406)
        elif is_vararg(leaf, within={syms.arglist, syms.argument}):
            _l_(6408)

            trailing_comma_safe = (
                trailing_comma_safe and Feature.TRAILING_COMMA_IN_CALL in features
            )
            _l_(6407)

    leaf_priority = bt.delimiters.get(id(leaf))
    _l_(6411)
    if leaf_priority == delimiter_priority:
        _l_(6414)

        aux = current_line
        _l_(6412)
        exit(aux)

        current_line = Line(
            mode=line.mode, depth=line.depth, inside_brackets=line.inside_brackets
        )
        _l_(6413)
if current_line:
    _l_(6420)

    if (
        trailing_comma_safe
        and delimiter_priority == COMMA_PRIORITY
        and current_line.leaves[-1].type != token.COMMA
        and current_line.leaves[-1].type != STANDALONE_COMMENT
    ):
        _l_(6418)

        new_comma = Leaf(token.COMMA, ",")
        _l_(6416)
        current_line.append(new_comma)
        _l_(6417)
    aux = current_line
    _l_(6419)
    exit(aux)
