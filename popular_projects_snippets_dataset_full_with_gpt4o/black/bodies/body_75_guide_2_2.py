import token # pragma: no cover
from typing import List # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type, value): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self, leaves, comments): # pragma: no cover
        self.leaves = leaves # pragma: no cover
        self.comments = comments # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves: List[Leaf]): # pragma: no cover
    def is_valid_index(i: int) -> bool: # pragma: no cover
        return 0 <= i < len(leaves) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
def has_triple_quotes(value: str) -> bool: # pragma: no cover
    return '"""' in value or "'''" in value # pragma: no cover
 # pragma: no cover
def get_string_prefix(value: str) -> str: # pragma: no cover
    if not value: # pragma: no cover
        return '' # pragma: no cover
    prefix_chars = '' # pragma: no cover
    for char in value: # pragma: no cover
        if char.lower() in 'frub': # pragma: no cover
            prefix_chars += char.lower() # pragma: no cover
        else: # pragma: no cover
            break # pragma: no cover
    return prefix_chars # pragma: no cover
 # pragma: no cover
def contains_pragma_comment(comment: str) -> bool: # pragma: no cover
    return 'pragma' in comment.lower() # pragma: no cover
 # pragma: no cover
class TErr(Exception): # pragma: no cover
    def __init__(self, msg): # pragma: no cover
        super().__init__(msg) # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
string_idx = 0 # pragma: no cover
STANDALONE_COMMENT = 999 # pragma: no cover
line = Line( # pragma: no cover
    leaves=[ # pragma: no cover
        Leaf(token.STRING, '"test_string1"'), # pragma: no cover
        Leaf(STANDALONE_COMMENT, '# standalone comment'), # pragma: no cover
        Leaf(token.STRING, '"test_string2"'), # pragma: no cover
        Leaf(token.COMMA, ',') # pragma: no cover
    ], # pragma: no cover
    comments={ # pragma: no cover
        id(Leaf(token.COMMA, ',')): '# pragma: no cover' # pragma: no cover
    } # pragma: no cover
) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""Validate (M)erge (S)tring (G)roup

        Transform-time string validation logic for _merge_string_group(...).

        Returns:
            * Ok(None), if ALL validation checks (listed below) pass.
                OR
            * Err(CannotTransform), if any of the following are true:
                - The target string group does not contain ANY stand-alone comments.
                - The target string is not in a string group (i.e. it has no
                  adjacent strings).
                - The string group has more than one inline comment.
                - The string group has an inline comment that appears to be a pragma.
                - The set of all string prefixes in the string group is of
                  length greater than one and is not equal to {"", "f"}.
                - The string group consists of raw strings.
                - The string group is stringified type annotations. We don't want to
                  process stringified type annotations since pyright doesn't support
                  them spanning multiple string values. (NOTE: mypy, pytype, pyre do
                  support them, so we can change if pyright also gains support in the
                  future. See https://github.com/microsoft/pyright/issues/4359.)
        """
# We first check for "inner" stand-alone comments (i.e. stand-alone
# comments that have a string leaf before them AND after them).
for inc in [1, -1]:
    _l_(17265)

    i = string_idx
    _l_(17256)
    found_sa_comment = False
    _l_(17257)
    is_valid_index = is_valid_index_factory(line.leaves)
    _l_(17258)
    while is_valid_index(i) and line.leaves[i].type in [
        token.STRING,
        STANDALONE_COMMENT,
    ]:
        _l_(17264)

        if line.leaves[i].type == STANDALONE_COMMENT:
            _l_(17262)

            found_sa_comment = True
            _l_(17259)
        elif found_sa_comment:
            _l_(17261)

            aux = TErr(
                "StringMerger does NOT merge string groups which contain "
                "stand-alone comments."
            )
            _l_(17260)
            exit(aux)

        i += inc
        _l_(17263)

num_of_inline_string_comments = 0
_l_(17266)
set_of_prefixes = set()
_l_(17267)
num_of_strings = 0
_l_(17268)
for leaf in line.leaves[string_idx:]:
    _l_(17284)

    if leaf.type != token.STRING:
        _l_(17272)

        # If the string group is trailed by a comma, we count the
        # comments trailing the comma to be one of the string group's
        # comments.
        if leaf.type == token.COMMA and id(leaf) in line.comments:
            _l_(17270)

            num_of_inline_string_comments += 1
            _l_(17269)
        break
        _l_(17271)

    if has_triple_quotes(leaf.value):
        _l_(17274)

        aux = TErr("StringMerger does NOT merge multiline strings.")
        _l_(17273)
        exit(aux)

    num_of_strings += 1
    _l_(17275)
    prefix = get_string_prefix(leaf.value).lower()
    _l_(17276)
    if "r" in prefix:
        _l_(17278)

        aux = TErr("StringMerger does NOT merge raw strings.")
        _l_(17277)
        exit(aux)

    set_of_prefixes.add(prefix)
    _l_(17279)

    if id(leaf) in line.comments:
        _l_(17283)

        num_of_inline_string_comments += 1
        _l_(17280)
        if contains_pragma_comment(line.comments[id(leaf)]):
            _l_(17282)

            aux = TErr("Cannot merge strings which have pragma comments.")
            _l_(17281)
            exit(aux)

if num_of_strings < 2:
    _l_(17286)

    aux = TErr(
        f"Not enough strings to merge (num_of_strings={num_of_strings})."
    )
    _l_(17285)
    exit(aux)

if num_of_inline_string_comments > 1:
    _l_(17288)

    aux = TErr(
        f"Too many inline string comments ({num_of_inline_string_comments})."
    )
    _l_(17287)
    exit(aux)

if len(set_of_prefixes) > 1 and set_of_prefixes != {"", "f"}:
    _l_(17290)

    aux = TErr(f"Too many different prefixes ({set_of_prefixes}).")
    _l_(17289)
    exit(aux)
aux = Ok(None)
_l_(17291)

exit(aux)
