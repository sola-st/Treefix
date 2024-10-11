from typing import List # pragma: no cover
import token # pragma: no cover

class Mock:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.line_length = 80# pragma: no cover
        self.depth = 0# pragma: no cover
        self.comments = []# pragma: no cover
# pragma: no cover
    def _get_string_operator_leaves(self, LL):# pragma: no cover
        return []# pragma: no cover
# pragma: no cover
    def pop_custom_splits(self, value):# pragma: no cover
        return []# pragma: no cover
# pragma: no cover
    def _get_break_idx(self, rest_value, max_bidx):# pragma: no cover
        return len(rest_value) // 2# pragma: no cover
# pragma: no cover
    def _normalize_f_string(self, next_value, prefix):# pragma: no cover
        return next_value# pragma: no cover
# pragma: no cover
    def _maybe_normalize_string_quotes(self, next_leaf):# pragma: no cover
        pass # pragma: no cover
line = Mock() # pragma: no cover
string_indices = [0] # pragma: no cover
self = Mock() # pragma: no cover
def is_valid_index_factory(LL):# pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
def insert_str_child_factory(leaf):# pragma: no cover
    return lambda child: None # pragma: no cover
def get_string_prefix(value):# pragma: no cover
    return value[:value.index('"')] if '"' in value else '' # pragma: no cover
def fstring_contains_expr(value):# pragma: no cover
    return False # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value # pragma: no cover
class Line:# pragma: no cover
    def clone(self):# pragma: no cover
        return Line() # pragma: no cover
TErr = Exception # pragma: no cover
Ok = lambda x: x # pragma: no cover

from typing import List # pragma: no cover
import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value # pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.leaves = [Leaf(token.STRING, 'Hello, '), Leaf(token.STRING, 'world!'), Leaf(token.COMMA, ',')]# pragma: no cover
        self.depth = 0# pragma: no cover
        self.comments = []# pragma: no cover
        # pragma: no cover
    def clone(self):# pragma: no cover
        return MockLine() # pragma: no cover
line = MockLine() # pragma: no cover
string_indices = [0] # pragma: no cover
self = type('MockSelf', (object,), {'line_length': 100, 'pop_custom_splits': lambda self, value: [], '_get_string_operator_leaves': lambda self, LL: [], '_get_break_idx': lambda self, rest_value, max_bidx: None, '_normalize_f_string': lambda self, value, prefix: value, '_maybe_normalize_string_quotes': lambda self, leaf: None})() # pragma: no cover
token = type('Token', (object,), {'STRING': 'string', 'COMMA': 'comma', 'LPAR': 'lpar'}) # pragma: no cover
def is_valid_index_factory(LL):# pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
insert_str_child_factory = lambda leaf: None # pragma: no cover
get_string_prefix = lambda value: value.strip()[:1] # pragma: no cover
def fstring_contains_expr(value):# pragma: no cover
    return False # pragma: no cover
TErr = Exception # pragma: no cover
Ok = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(3924)
assert len(string_indices) == 1, (
    f"{self.__class__.__name__} should only find one match at a time, found"
    f" {len(string_indices)}"
)
_l_(3925)
string_idx = string_indices[0]
_l_(3926)

QUOTE = LL[string_idx].value[-1]
_l_(3927)

is_valid_index = is_valid_index_factory(LL)
_l_(3928)
insert_str_child = insert_str_child_factory(LL[string_idx])
_l_(3929)

prefix = get_string_prefix(LL[string_idx].value).lower()
_l_(3930)

# We MAY choose to drop the 'f' prefix from substrings that don't
# contain any f-expressions, but ONLY if the original f-string
# contains at least one f-expression. Otherwise, we will alter the AST
# of the program.
drop_pointless_f_prefix = ("f" in prefix) and fstring_contains_expr(
    LL[string_idx].value
)
_l_(3931)

first_string_line = True
_l_(3932)

string_op_leaves = self._get_string_operator_leaves(LL)
_l_(3933)
string_op_leaves_length = (
    sum(len(str(prefix_leaf)) for prefix_leaf in string_op_leaves) + 1
    if string_op_leaves
    else 0
)
_l_(3934)

def maybe_append_string_operators(new_line: Line) -> None:
    _l_(3939)

    """
            Side Effects:
                If @line starts with a string operator and this is the first
                line we are constructing, this function appends the string
                operator to @new_line and replaces the old string operator leaf
                in the node structure. Otherwise this function does nothing.
            """
    maybe_prefix_leaves = string_op_leaves if first_string_line else []
    _l_(3935)
    for i, prefix_leaf in enumerate(maybe_prefix_leaves):
        _l_(3938)

        replace_child(LL[i], prefix_leaf)
        _l_(3936)
        new_line.append(prefix_leaf)
        _l_(3937)

ends_with_comma = (
    is_valid_index(string_idx + 1) and LL[string_idx + 1].type == token.COMMA
)
_l_(3940)

def max_last_string() -> int:
    _l_(3946)

    """
            Returns:
                The max allowed length of the string value used for the last
                line we will construct.
            """
    result = self.line_length
    _l_(3941)
    result -= line.depth * 4
    _l_(3942)
    result -= 1 if ends_with_comma else 0
    _l_(3943)
    result -= string_op_leaves_length
    _l_(3944)
    aux = result
    _l_(3945)
    exit(aux)

# --- Calculate Max Break Index (for string value)
# We start with the line length limit
max_break_idx = self.line_length
_l_(3947)
# The last index of a string of length N is N-1.
max_break_idx -= 1
_l_(3948)
# Leading whitespace is not present in the string value (e.g. Leaf.value).
max_break_idx -= line.depth * 4
_l_(3949)
if max_break_idx < 0:
    _l_(3952)

    aux = TErr(
        f"Unable to split {LL[string_idx].value} at such high of a line depth:"
        f" {line.depth}"
    )
    _l_(3950)
    exit(aux)
    exit()
    _l_(3951)

# Check if StringMerger registered any custom splits.
custom_splits = self.pop_custom_splits(LL[string_idx].value)
_l_(3953)
# We use them ONLY if none of them would produce lines that exceed the
# line limit.
use_custom_breakpoints = bool(
    custom_splits
    and all(csplit.break_idx <= max_break_idx for csplit in custom_splits)
)
_l_(3954)

# Temporary storage for the remaining chunk of the string line that
# can't fit onto the line currently being constructed.
rest_value = LL[string_idx].value
_l_(3955)

def more_splits_should_be_made() -> bool:
    _l_(3959)

    """
            Returns:
                True iff `rest_value` (the remaining string value from the last
                split), should be split again.
            """
    if use_custom_breakpoints:
        _l_(3958)

        aux = len(custom_splits) > 1
        _l_(3956)
        exit(aux)
    else:
        aux = len(rest_value) > max_last_string()
        _l_(3957)
        exit(aux)

string_line_results: List[Ok[Line]] = []
_l_(3960)
while more_splits_should_be_made():
    _l_(3990)

    if use_custom_breakpoints:
        _l_(3974)

        # Custom User Split (manual)
        csplit = custom_splits.pop(0)
        _l_(3961)
        break_idx = csplit.break_idx
        _l_(3962)
    else:
        # Algorithmic Split (automatic)
        max_bidx = max_break_idx - string_op_leaves_length
        _l_(3963)
        maybe_break_idx = self._get_break_idx(rest_value, max_bidx)
        _l_(3964)
        if maybe_break_idx is None:
            _l_(3972)

            # If we are unable to algorithmically determine a good split
            # and this string has custom splits registered to it, we
            # fall back to using them--which means we have to start
            # over from the beginning.
            if custom_splits:
                _l_(3970)

                rest_value = LL[string_idx].value
                _l_(3965)
                string_line_results = []
                _l_(3966)
                first_string_line = True
                _l_(3967)
                use_custom_breakpoints = True
                _l_(3968)
                continue
                _l_(3969)

            # Otherwise, we stop splitting here.
            break
            _l_(3971)

        break_idx = maybe_break_idx
        _l_(3973)

    # --- Construct `next_value`
    next_value = rest_value[:break_idx] + QUOTE
    _l_(3975)

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
        _l_(3978)

        # Then `csplit.break_idx` will be off by one after removing
        # the 'f' prefix.
        break_idx += 1
        _l_(3976)
        next_value = rest_value[:break_idx] + QUOTE
        _l_(3977)

    if drop_pointless_f_prefix:
        _l_(3980)

        next_value = self._normalize_f_string(next_value, prefix)
        _l_(3979)

    # --- Construct `next_leaf`
    next_leaf = Leaf(token.STRING, next_value)
    _l_(3981)
    insert_str_child(next_leaf)
    _l_(3982)
    self._maybe_normalize_string_quotes(next_leaf)
    _l_(3983)

    # --- Construct `next_line`
    next_line = line.clone()
    _l_(3984)
    maybe_append_string_operators(next_line)
    _l_(3985)
    next_line.append(next_leaf)
    _l_(3986)
    string_line_results.append(Ok(next_line))
    _l_(3987)

    rest_value = prefix + QUOTE + rest_value[break_idx:]
    _l_(3988)
    first_string_line = False
    _l_(3989)
aux = string_line_results
_l_(3991)

exit(aux)

if drop_pointless_f_prefix:
    _l_(3993)

    rest_value = self._normalize_f_string(rest_value, prefix)
    _l_(3992)

rest_leaf = Leaf(token.STRING, rest_value)
_l_(3994)
insert_str_child(rest_leaf)
_l_(3995)

# NOTE: I could not find a test case that verifies that the following
# line is actually necessary, but it seems to be. Otherwise we risk
# not normalizing the last substring, right?
self._maybe_normalize_string_quotes(rest_leaf)
_l_(3996)

last_line = line.clone()
_l_(3997)
maybe_append_string_operators(last_line)
_l_(3998)

# If there are any leaves to the right of the target string...
if is_valid_index(string_idx + 1):
    _l_(4016)

    # We use `temp_value` here to determine how long the last line
    # would be if we were to append all the leaves to the right of the
    # target string to the last string line.
    temp_value = rest_value
    _l_(3999)
    for leaf in LL[string_idx + 1 :]:
        _l_(4003)

        temp_value += str(leaf)
        _l_(4000)
        if leaf.type == token.LPAR:
            _l_(4002)

            break
            _l_(4001)
    if (
        len(temp_value) <= max_last_string()
        or LL[string_idx + 1].type == token.COMMA
    ):
        _l_(4012)

        last_line.append(rest_leaf)
        _l_(4004)
        append_leaves(last_line, line, LL[string_idx + 1 :])
        _l_(4005)
        aux = Ok(last_line)
        _l_(4006)
        exit(aux)
    # Otherwise, place the last substring on one line and everything
    # else on a line below that...
    else:
        last_line.append(rest_leaf)
        _l_(4007)
        aux = Ok(last_line)
        _l_(4008)
        exit(aux)

        non_string_line = line.clone()
        _l_(4009)
        append_leaves(non_string_line, line, LL[string_idx + 1 :])
        _l_(4010)
        aux = Ok(non_string_line)
        _l_(4011)
        exit(aux)
        # Else the target string was the last leaf...
else:
    last_line.append(rest_leaf)
    _l_(4013)
    last_line.comments = line.comments.copy()
    _l_(4014)
    aux = Ok(last_line)
    _l_(4015)
    exit(aux)
