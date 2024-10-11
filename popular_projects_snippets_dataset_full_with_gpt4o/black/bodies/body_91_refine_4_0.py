from typing import List # pragma: no cover
from collections import namedtuple # pragma: no cover
import token # pragma: no cover

line = type('MockLine', (object,), {'leaves': [type('MockLeaf', (object,), {'value': 'test'})()]})() # pragma: no cover
string_indices = [0] # pragma: no cover
self = type('MockSelf', (object,), {'__class__': type('MockClass', (object,), {'__name__': 'MockClass'}), '_get_string_operator_leaves': lambda self, x: [], 'line_length': 80, 'pop_custom_splits': lambda self, x: [], '_get_break_idx': lambda self, x, y: None, '_normalize_f_string': lambda self, x, y: x, '_maybe_normalize_string_quotes': lambda self, x: None})() # pragma: no cover
is_valid_index_factory = lambda x: lambda idx: idx < len(x) # pragma: no cover
insert_str_child_factory = lambda x: lambda y: None # pragma: no cover
get_string_prefix = lambda x: 'f' # pragma: no cover
fstring_contains_expr = lambda x: '{' in x and '}' in x # pragma: no cover
Line = type('MockLineClass', (object,), {'clone': lambda self: self, 'append': lambda self, leaf: None, 'comments': []}) # pragma: no cover
TErr = namedtuple('TErr', 'msg') # pragma: no cover
Ok = namedtuple('Ok', 'line') # pragma: no cover
Leaf = namedtuple('Leaf', 'type value') # pragma: no cover
append_leaves = lambda line, original_line, leaves: None # pragma: no cover
replace_child = lambda old_leaf, new_leaf: None # pragma: no cover

from typing import List, Any # pragma: no cover
from collections import namedtuple # pragma: no cover
import token # pragma: no cover

MockLeaf = type('MockLeaf', (object,), {'value': 'mock_value', 'type': token.STRING}) # pragma: no cover
line = type('MockLine', (object,), {'leaves': [MockLeaf() for _ in range(10)], 'depth': 1, 'clone': lambda self: self, 'comments': {}})() # pragma: no cover
string_indices = [0] # pragma: no cover
self = type('MockSelf', (object,), {'__class__': type('MockClass', (object,), {'__name__': 'MockClass'}), '_get_string_operator_leaves': lambda self, LL: [], 'line_length': 80, 'pop_custom_splits': lambda value: [], '_get_break_idx': lambda rest_value, max_bidx: 0, '_normalize_f_string': lambda next_value, prefix: next_value, '_maybe_normalize_string_quotes': lambda leaf: None})() # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover
insert_str_child_factory = lambda leaf: lambda child: None # pragma: no cover
get_string_prefix = lambda value: 'f' # pragma: no cover
fstring_contains_expr = lambda value: '{' in value and '}' in value # pragma: no cover
Line = type('MockLineClass', (object,), {'append': lambda self, item: None, 'clone': lambda self: self}) # pragma: no cover
TErr = namedtuple('TErr', 'msg') # pragma: no cover
Ok = namedtuple('Ok', 'value') # pragma: no cover
Leaf = namedtuple('Leaf', 'type value') # pragma: no cover
append_leaves = lambda last_line, line, leaves: None # pragma: no cover
replace_child = lambda old_leaf, new_leaf: None # pragma: no cover
token.COMMA = 54 # pragma: no cover
token.STRING = 3 # pragma: no cover
token.LPAR = 7 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(15717)
assert len(string_indices) == 1, (
    f"{self.__class__.__name__} should only find one match at a time, found"
    f" {len(string_indices)}"
)
_l_(15718)
string_idx = string_indices[0]
_l_(15719)

QUOTE = LL[string_idx].value[-1]
_l_(15720)

is_valid_index = is_valid_index_factory(LL)
_l_(15721)
insert_str_child = insert_str_child_factory(LL[string_idx])
_l_(15722)

prefix = get_string_prefix(LL[string_idx].value).lower()
_l_(15723)

# We MAY choose to drop the 'f' prefix from substrings that don't
# contain any f-expressions, but ONLY if the original f-string
# contains at least one f-expression. Otherwise, we will alter the AST
# of the program.
drop_pointless_f_prefix = ("f" in prefix) and fstring_contains_expr(
    LL[string_idx].value
)
_l_(15724)

first_string_line = True
_l_(15725)

string_op_leaves = self._get_string_operator_leaves(LL)
_l_(15726)
string_op_leaves_length = (
    sum(len(str(prefix_leaf)) for prefix_leaf in string_op_leaves) + 1
    if string_op_leaves
    else 0
)
_l_(15727)

def maybe_append_string_operators(new_line: Line) -> None:
    _l_(15732)

    """
            Side Effects:
                If @line starts with a string operator and this is the first
                line we are constructing, this function appends the string
                operator to @new_line and replaces the old string operator leaf
                in the node structure. Otherwise this function does nothing.
            """
    maybe_prefix_leaves = string_op_leaves if first_string_line else []
    _l_(15728)
    for i, prefix_leaf in enumerate(maybe_prefix_leaves):
        _l_(15731)

        replace_child(LL[i], prefix_leaf)
        _l_(15729)
        new_line.append(prefix_leaf)
        _l_(15730)

ends_with_comma = (
    is_valid_index(string_idx + 1) and LL[string_idx + 1].type == token.COMMA
)
_l_(15733)

def max_last_string() -> int:
    _l_(15739)

    """
            Returns:
                The max allowed length of the string value used for the last
                line we will construct.
            """
    result = self.line_length
    _l_(15734)
    result -= line.depth * 4
    _l_(15735)
    result -= 1 if ends_with_comma else 0
    _l_(15736)
    result -= string_op_leaves_length
    _l_(15737)
    aux = result
    _l_(15738)
    exit(aux)

# --- Calculate Max Break Index (for string value)
# We start with the line length limit
max_break_idx = self.line_length
_l_(15740)
# The last index of a string of length N is N-1.
max_break_idx -= 1
_l_(15741)
# Leading whitespace is not present in the string value (e.g. Leaf.value).
max_break_idx -= line.depth * 4
_l_(15742)
if max_break_idx < 0:
    _l_(15745)

    aux = TErr(
        f"Unable to split {LL[string_idx].value} at such high of a line depth:"
        f" {line.depth}"
    )
    _l_(15743)
    exit(aux)
    exit()
    _l_(15744)

# Check if StringMerger registered any custom splits.
custom_splits = self.pop_custom_splits(LL[string_idx].value)
_l_(15746)
# We use them ONLY if none of them would produce lines that exceed the
# line limit.
use_custom_breakpoints = bool(
    custom_splits
    and all(csplit.break_idx <= max_break_idx for csplit in custom_splits)
)
_l_(15747)

# Temporary storage for the remaining chunk of the string line that
# can't fit onto the line currently being constructed.
rest_value = LL[string_idx].value
_l_(15748)

def more_splits_should_be_made() -> bool:
    _l_(15752)

    """
            Returns:
                True iff `rest_value` (the remaining string value from the last
                split), should be split again.
            """
    if use_custom_breakpoints:
        _l_(15751)

        aux = len(custom_splits) > 1
        _l_(15749)
        exit(aux)
    else:
        aux = len(rest_value) > max_last_string()
        _l_(15750)
        exit(aux)

string_line_results: List[Ok[Line]] = []
_l_(15753)
while more_splits_should_be_made():
    _l_(15783)

    if use_custom_breakpoints:
        _l_(15767)

        # Custom User Split (manual)
        csplit = custom_splits.pop(0)
        _l_(15754)
        break_idx = csplit.break_idx
        _l_(15755)
    else:
        # Algorithmic Split (automatic)
        max_bidx = max_break_idx - string_op_leaves_length
        _l_(15756)
        maybe_break_idx = self._get_break_idx(rest_value, max_bidx)
        _l_(15757)
        if maybe_break_idx is None:
            _l_(15765)

            # If we are unable to algorithmically determine a good split
            # and this string has custom splits registered to it, we
            # fall back to using them--which means we have to start
            # over from the beginning.
            if custom_splits:
                _l_(15763)

                rest_value = LL[string_idx].value
                _l_(15758)
                string_line_results = []
                _l_(15759)
                first_string_line = True
                _l_(15760)
                use_custom_breakpoints = True
                _l_(15761)
                continue
                _l_(15762)

            # Otherwise, we stop splitting here.
            break
            _l_(15764)

        break_idx = maybe_break_idx
        _l_(15766)

    # --- Construct `next_value`
    next_value = rest_value[:break_idx] + QUOTE
    _l_(15768)

    # HACK: The following 'if' statement is a hack to fix the custom
    # breakpoint index in the case of either: (a) substrings that were
    # f-strings but will have the 'f' prefix removed OR (b) substrings
    # that were not f-strings but will now become f-strings because of
    # redundant use of the 'f' prefix (i.e. none of the substrings
    # contain f-expressions but one or more of them had the 'f' prefix
    # anyway; in which case, we will prepend 'f' to _all_ substrings).
    #
    # There is probably a better way to accomplish what is being done
    # here...
    #
    # If this substring is an f-string, we _could_ remove the 'f'
    # prefix, and the current custom split did NOT originally use a
    # prefix...
    if (
        use_custom_breakpoints
        and not csplit.has_prefix
        and (
            # `next_value == prefix + QUOTE` happens when the custom
            # split is an empty string.
            next_value == prefix + QUOTE
            or next_value != self._normalize_f_string(next_value, prefix)
        )
    ):
        _l_(15771)

        # Then `csplit.break_idx` will be off by one after removing
        # the 'f' prefix.
        break_idx += 1
        _l_(15769)
        next_value = rest_value[:break_idx] + QUOTE
        _l_(15770)

    if drop_pointless_f_prefix:
        _l_(15773)

        next_value = self._normalize_f_string(next_value, prefix)
        _l_(15772)

    # --- Construct `next_leaf`
    next_leaf = Leaf(token.STRING, next_value)
    _l_(15774)
    insert_str_child(next_leaf)
    _l_(15775)
    self._maybe_normalize_string_quotes(next_leaf)
    _l_(15776)

    # --- Construct `next_line`
    next_line = line.clone()
    _l_(15777)
    maybe_append_string_operators(next_line)
    _l_(15778)
    next_line.append(next_leaf)
    _l_(15779)
    string_line_results.append(Ok(next_line))
    _l_(15780)

    rest_value = prefix + QUOTE + rest_value[break_idx:]
    _l_(15781)
    first_string_line = False
    _l_(15782)
aux = string_line_results
_l_(15784)

exit(aux)

if drop_pointless_f_prefix:
    _l_(15786)

    rest_value = self._normalize_f_string(rest_value, prefix)
    _l_(15785)

rest_leaf = Leaf(token.STRING, rest_value)
_l_(15787)
insert_str_child(rest_leaf)
_l_(15788)

# NOTE: I could not find a test case that verifies that the following
# line is actually necessary, but it seems to be. Otherwise we risk
# not normalizing the last substring, right?
self._maybe_normalize_string_quotes(rest_leaf)
_l_(15789)

last_line = line.clone()
_l_(15790)
maybe_append_string_operators(last_line)
_l_(15791)

# If there are any leaves to the right of the target string...
if is_valid_index(string_idx + 1):
    _l_(15809)

    # We use `temp_value` here to determine how long the last line
    # would be if we were to append all the leaves to the right of the
    # target string to the last string line.
    temp_value = rest_value
    _l_(15792)
    for leaf in LL[string_idx + 1 :]:
        _l_(15796)

        temp_value += str(leaf)
        _l_(15793)
        if leaf.type == token.LPAR:
            _l_(15795)

            break
            _l_(15794)
    if (
        len(temp_value) <= max_last_string()
        or LL[string_idx + 1].type == token.COMMA
    ):
        _l_(15805)

        last_line.append(rest_leaf)
        _l_(15797)
        append_leaves(last_line, line, LL[string_idx + 1 :])
        _l_(15798)
        aux = Ok(last_line)
        _l_(15799)
        exit(aux)
    # Otherwise, place the last substring on one line and everything
    # else on a line below that...
    else:
        last_line.append(rest_leaf)
        _l_(15800)
        aux = Ok(last_line)
        _l_(15801)
        exit(aux)

        non_string_line = line.clone()
        _l_(15802)
        append_leaves(non_string_line, line, LL[string_idx + 1 :])
        _l_(15803)
        aux = Ok(non_string_line)
        _l_(15804)
        exit(aux)
        # Else the target string was the last leaf...
else:
    last_line.append(rest_leaf)
    _l_(15806)
    last_line.comments = line.comments.copy()
    _l_(15807)
    aux = Ok(last_line)
    _l_(15808)
    exit(aux)
