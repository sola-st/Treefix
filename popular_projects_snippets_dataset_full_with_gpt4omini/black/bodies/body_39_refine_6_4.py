from typing import Iterator # pragma: no cover
import sys # pragma: no cover
import token # pragma: no cover

line = type('MockLine', (object,), {'leaves': [], 'bracket_tracker': type('MockBracketTracker', (object,), {'max_delimiter_priority': lambda self, exclude: 0, 'delimiter_count_with_priority': lambda self, priority: 0, 'delimiters': {}})(), 'mode': 'some_mode', 'depth': 0, 'inside_brackets': False, 'comments_after': lambda self, leaf: []})() # pragma: no cover
class CannotSplit(Exception): pass # pragma: no cover
DOT_PRIORITY = 0 # pragma: no cover
class Line(object):# pragma: no cover
    def __init__(self, mode, depth, inside_brackets):# pragma: no cover
        self.leaves = []# pragma: no cover
        self.mode = mode# pragma: no cover
        self.depth = depth# pragma: no cover
        self.inside_brackets = inside_brackets# pragma: no cover
    def append_safe(self, leaf, preformatted=False):# pragma: no cover
        self.leaves.append(leaf)# pragma: no cover
    def append(self, leaf):# pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
Leaf = type('MockLeaf', (object,), {'bracket_depth': 0, 'type': None}) # pragma: no cover
is_vararg = lambda leaf, within: False # pragma: no cover
syms = type('MockSyms', (object,), {'typedargslist': 'typedargslist', 'arglist': 'arglist', 'argument': 'argument'})() # pragma: no cover
class Feature(object):# pragma: no cover
    TRAILING_COMMA_IN_DEF = 'trailing_comma_in_def'# pragma: no cover
    TRAILING_COMMA_IN_CALL = 'trailing_comma_in_call' # pragma: no cover
features = {Feature.TRAILING_COMMA_IN_DEF, Feature.TRAILING_COMMA_IN_CALL} # pragma: no cover
COMMA_PRIORITY = 1 # pragma: no cover
STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover

from typing import Iterator # pragma: no cover
import sys # pragma: no cover
import token # pragma: no cover

class CannotSplit(Exception): pass # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def max_delimiter_priority(self, exclude): return 1# pragma: no cover
    def delimiter_count_with_priority(self, priority): return 1# pragma: no cover
    def __init__(self): self.delimiters = {} # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, leaf_type):# pragma: no cover
        self.type = leaf_type# pragma: no cover
        self.bracket_depth = 0 # pragma: no cover
class Line:# pragma: no cover
    def __init__(self, mode, depth, inside_brackets):# pragma: no cover
        self.leaves = []# pragma: no cover
        self.mode = mode# pragma: no cover
        self.depth = depth# pragma: no cover
        self.inside_brackets = inside_brackets# pragma: no cover
    # pragma: no cover
    def append_safe(self, leaf, preformatted=False):# pragma: no cover
        self.leaves.append(leaf)# pragma: no cover
    # pragma: no cover
    def append(self, leaf):# pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
line = Line('test_mode', 0, False)# pragma: no cover
line.bracket_tracker = MockBracketTracker() # pragma: no cover
current_line = Line(line.mode, line.depth, line.inside_brackets) # pragma: no cover
DOT_PRIORITY = 1 # pragma: no cover
COMMA_PRIORITY = 2 # pragma: no cover
features = {1, 2} # pragma: no cover
class Feature:# pragma: no cover
    TRAILING_COMMA_IN_DEF = 1# pragma: no cover
    TRAILING_COMMA_IN_CALL = 2 # pragma: no cover
syms = type('syms', (object,), {'typedargslist': 1, 'arglist': 2, 'argument': 3}) # pragma: no cover
token = type('token', (object,), {'COMMA': 1, 'STANDALONE_COMMENT': 2}) # pragma: no cover
STANDALONE_COMMENT = 2 # pragma: no cover
is_vararg = lambda leaf, within: False # pragma: no cover

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
