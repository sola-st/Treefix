from types import SimpleNamespace # pragma: no cover
import token # pragma: no cover

line = SimpleNamespace( # pragma: no cover
    leaves=[SimpleNamespace(type=token.NAME, value='a'), SimpleNamespace(type=token.LPAR, value=''), SimpleNamespace(type=token.STRING, value='hello'), SimpleNamespace(type=token.RPAR, value='')], # pragma: no cover
    depth=1, # pragma: no cover
    comments_after=lambda idx: [] # pragma: no cover
) # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover
string_idx = 2 # pragma: no cover
class SelfMock: # pragma: no cover
    STRING_OPERATORS = {token.PLUS, token.EQUAL} # pragma: no cover
    line_length = 80 # pragma: no cover
self = SelfMock() # pragma: no cover
CLOSING_BRACKETS = {token.RPAR, token.RSQB, token.RBRACE} # pragma: no cover

import token # pragma: no cover

MockLeaf = type('MockLeaf', (object,), {'__init__': lambda self, _type, value: setattr(self, 'type', _type) or setattr(self, 'value', value)}) # pragma: no cover
MockLine = type('MockLine', (object,), {'leaves': [MockLeaf(token.NAME, 'a'), MockLeaf(token.LPAR, ''), MockLeaf(token.STRING, 'string'), MockLeaf(token.RPAR, '')], 'depth': 2, 'comments_after': lambda self, x: [MockLeaf(token.COMMENT, '# This is a comment')]}) # pragma: no cover
line = MockLine() # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover
string_idx = 2 # pragma: no cover
self = type('SelfMock', (object,), {'STRING_OPERATORS': [token.PLUS, token.EQUAL], 'line_length': 80})() # pragma: no cover
CLOSING_BRACKETS = [token.RPAR, token.RBRACE, token.RSQB] # pragma: no cover

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
_l_(19768)

is_valid_index = is_valid_index_factory(LL)
_l_(19769)

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
_l_(19770)

if is_valid_index(string_idx - 1):
    _l_(19785)

    p_idx = string_idx - 1
    _l_(19771)
    if (
        LL[string_idx - 1].type == token.LPAR
        and LL[string_idx - 1].value == ""
        and string_idx >= 2
    ):
        _l_(19773)

        # If the previous leaf is an empty LPAR placeholder, we should skip it.
        p_idx -= 1
        _l_(19772)

    P = LL[p_idx]
    _l_(19774)
    if P.type in self.STRING_OPERATORS:
        _l_(19776)

        # WMA4 a space and a string operator (e.g. `+ STRING` or `== STRING`).
        offset += len(str(P)) + 1
        _l_(19775)

    if P.type == token.COMMA:
        _l_(19778)

        # WMA4 a space, a comma, and a closing bracket [e.g. `), STRING`].
        offset += 3
        _l_(19777)

    if P.type in [token.COLON, token.EQUAL, token.PLUSEQUAL, token.NAME]:
        _l_(19784)

        # This conditional branch is meant to handle dictionary keys,
        # variable assignments, 'return STRING' statement lines, and
        # 'else STRING' ternary expression lines.

        # WMA4 a single space.
        offset += 1
        _l_(19779)

        # WMA4 the lengths of any leaves that came before that space,
        # but after any closing bracket before that space.
        for leaf in reversed(LL[: p_idx + 1]):
            _l_(19783)

            offset += len(str(leaf))
            _l_(19780)
            if leaf.type in CLOSING_BRACKETS:
                _l_(19782)

                break
                _l_(19781)

if is_valid_index(string_idx + 1):
    _l_(19798)

    N = LL[string_idx + 1]
    _l_(19786)
    if N.type == token.RPAR and N.value == "" and len(LL) > string_idx + 2:
        _l_(19788)

        # If the next leaf is an empty RPAR placeholder, we should skip it.
        N = LL[string_idx + 2]
        _l_(19787)

    if N.type == token.COMMA:
        _l_(19790)

        # WMA4 a single comma at the end of the string (e.g `STRING,`).
        offset += 1
        _l_(19789)

    if is_valid_index(string_idx + 2):
        _l_(19797)

        NN = LL[string_idx + 2]
        _l_(19791)

        if N.type == token.DOT and NN.type == token.NAME:
            _l_(19796)

            # This conditional branch is meant to handle method calls invoked
            # off of a string literal up to and including the LPAR character.

            # WMA4 the '.' character.
            offset += 1
            _l_(19792)

            if (
                is_valid_index(string_idx + 3)
                and LL[string_idx + 3].type == token.LPAR
            ):
                _l_(19794)

                # WMA4 the left parenthesis character.
                offset += 1
                _l_(19793)

            # WMA4 the length of the method's name.
            offset += len(NN.value)
            _l_(19795)

has_comments = False
_l_(19799)
for comment_leaf in line.comments_after(LL[string_idx]):
    _l_(19804)

    if not has_comments:
        _l_(19802)

        has_comments = True
        _l_(19800)
        # WMA4 two spaces before the '#' character.
        offset += 2
        _l_(19801)

    # WMA4 the length of the inline comment.
    offset += len(comment_leaf.value)
    _l_(19803)

max_string_length = self.line_length - offset
_l_(19805)
aux = max_string_length
_l_(19806)
exit(aux)
