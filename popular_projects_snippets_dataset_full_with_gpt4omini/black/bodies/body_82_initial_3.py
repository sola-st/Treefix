import token # pragma: no cover

class MockLine:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [] # pragma: no cover
        self.depth = 0 # pragma: no cover
        self.line_length = 80 # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return [] # pragma: no cover
line = MockLine() # pragma: no cover
for i in range(5): # pragma: no cover
    line.leaves.append(type('MockLeaf', (object,), {'type': token.STRING, 'value': f'string_{i}'})) # pragma: no cover
is_valid_index_factory = lambda leaves: lambda idx: 0 <= idx < len(leaves) # pragma: no cover
string_idx = 2 # pragma: no cover
token.LPAR = 'LPAR' # pragma: no cover
token.RPAR = 'RPAR' # pragma: no cover
token.COMMA = 'COMMA' # pragma: no cover
token.COLON = 'COLON' # pragma: no cover
token.EQUAL = 'EQUAL' # pragma: no cover
token.PLUSEQUAL = 'PLUSEQUAL' # pragma: no cover
token.NAME = 'NAME' # pragma: no cover
token.DOT = 'DOT' # pragma: no cover
self = type('MockSelf', (object,), {'STRING_OPERATORS': [token.EQUAL, token.PLUSEQUAL], 'line_length': 80})() # pragma: no cover
CLOSING_BRACKETS = [')', '}', ']'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Calculates the max string length used when attempting to determine
        whether or not the target string is responsible for causing the line to
        go over the line length limit.

        WARNING: This method is tightly coupled to both StringSplitter and
        (especially) StringParenWrapper. There is probably a better way to
        accomplish what is being done here.

        Returns:
            max_string_length: such that `line.leaves[string_idx].value >
            max_string_length` implies that the target string IS responsible
            for causing this line to exceed the line length limit.
        """
LL = line.leaves
_l_(8285)

is_valid_index = is_valid_index_factory(LL)
_l_(8286)

# We use the shorthand "WMA4" in comments to abbreviate "We must
# account for". When giving examples, we use STRING to mean some/any
# valid string.
#
# Finally, we use the following convenience variables:
#
#   P:  The leaf that is before the target string leaf.
#   N:  The leaf that is after the target string leaf.
#   NN: The leaf that is after N.

# WMA4 the whitespace at the beginning of the line.
offset = line.depth * 4
_l_(8287)

if is_valid_index(string_idx - 1):
    _l_(8302)

    p_idx = string_idx - 1
    _l_(8288)
    if (
        LL[string_idx - 1].type == token.LPAR
        and LL[string_idx - 1].value == ""
        and string_idx >= 2
    ):
        _l_(8290)

        # If the previous leaf is an empty LPAR placeholder, we should skip it.
        p_idx -= 1
        _l_(8289)

    P = LL[p_idx]
    _l_(8291)
    if P.type in self.STRING_OPERATORS:
        _l_(8293)

        # WMA4 a space and a string operator (e.g. `+ STRING` or `== STRING`).
        offset += len(str(P)) + 1
        _l_(8292)

    if P.type == token.COMMA:
        _l_(8295)

        # WMA4 a space, a comma, and a closing bracket [e.g. `), STRING`].
        offset += 3
        _l_(8294)

    if P.type in [token.COLON, token.EQUAL, token.PLUSEQUAL, token.NAME]:
        _l_(8301)

        # This conditional branch is meant to handle dictionary keys,
        # variable assignments, 'return STRING' statement lines, and
        # 'else STRING' ternary expression lines.

        # WMA4 a single space.
        offset += 1
        _l_(8296)

        # WMA4 the lengths of any leaves that came before that space,
        # but after any closing bracket before that space.
        for leaf in reversed(LL[: p_idx + 1]):
            _l_(8300)

            offset += len(str(leaf))
            _l_(8297)
            if leaf.type in CLOSING_BRACKETS:
                _l_(8299)

                break
                _l_(8298)

if is_valid_index(string_idx + 1):
    _l_(8315)

    N = LL[string_idx + 1]
    _l_(8303)
    if N.type == token.RPAR and N.value == "" and len(LL) > string_idx + 2:
        _l_(8305)

        # If the next leaf is an empty RPAR placeholder, we should skip it.
        N = LL[string_idx + 2]
        _l_(8304)

    if N.type == token.COMMA:
        _l_(8307)

        # WMA4 a single comma at the end of the string (e.g `STRING,`).
        offset += 1
        _l_(8306)

    if is_valid_index(string_idx + 2):
        _l_(8314)

        NN = LL[string_idx + 2]
        _l_(8308)

        if N.type == token.DOT and NN.type == token.NAME:
            _l_(8313)

            # This conditional branch is meant to handle method calls invoked
            # off of a string literal up to and including the LPAR character.

            # WMA4 the '.' character.
            offset += 1
            _l_(8309)

            if (
                is_valid_index(string_idx + 3)
                and LL[string_idx + 3].type == token.LPAR
            ):
                _l_(8311)

                # WMA4 the left parenthesis character.
                offset += 1
                _l_(8310)

            # WMA4 the length of the method's name.
            offset += len(NN.value)
            _l_(8312)

has_comments = False
_l_(8316)
for comment_leaf in line.comments_after(LL[string_idx]):
    _l_(8321)

    if not has_comments:
        _l_(8319)

        has_comments = True
        _l_(8317)
        # WMA4 two spaces before the '#' character.
        offset += 2
        _l_(8318)

    # WMA4 the length of the inline comment.
    offset += len(comment_leaf.value)
    _l_(8320)

max_string_length = self.line_length - offset
_l_(8322)
aux = max_string_length
_l_(8323)
exit(aux)
