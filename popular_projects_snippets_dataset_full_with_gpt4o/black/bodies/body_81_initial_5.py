from typing import List, Optional # pragma: no cover
from dataclasses import dataclass # pragma: no cover
from enum import Enum # pragma: no cover

@dataclass# pragma: no cover
class Line:# pragma: no cover
    leaves: List['StringLeaf']# pragma: no cover
    comments: dict # pragma: no cover
@dataclass# pragma: no cover
class StringLeaf:# pragma: no cover
    value: str# pragma: no cover
    parent: Optional['StringLeaf']# pragma: no cover
    children: List['StringLeaf']# pragma: no cover
    type: 'TokenType' # pragma: no cover
class TokenType(Enum):# pragma: no cover
    STRING = 1# pragma: no cover
    NEWLINE = 2 # pragma: no cover
class SelfMock:# pragma: no cover
    def _get_max_string_length(self, line, string_idx):# pragma: no cover
        return 80 # pragma: no cover
line = Line(leaves=[StringLeaf(value='test', parent=None, children=[], type=TokenType.STRING)], comments={}) # pragma: no cover
string_idx = 0 # pragma: no cover
self = SelfMock() # pragma: no cover
class TErr(Exception):# pragma: no cover
    pass # pragma: no cover
token = TokenType # pragma: no cover
def contains_pragma_comment(comment):# pragma: no cover
    return 'pragma' in comment # pragma: no cover
def has_triple_quotes(string):# pragma: no cover
    return '"""' in string or "'''" in string # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Checks that @line meets all of the requirements listed in this classes'
        docstring. Refer to `help(BaseStringSplitter)` for a detailed
        description of those requirements.

        Returns:
            * Ok(None), if ALL of the requirements are met.
                OR
            * Err(CannotTransform), if ANY of the requirements are NOT met.
        """
LL = line.leaves
_l_(19542)

string_leaf = LL[string_idx]
_l_(19543)

max_string_length = self._get_max_string_length(line, string_idx)
_l_(19544)
if len(string_leaf.value) <= max_string_length:
    _l_(19546)

    aux = TErr(
        "The string itself is not what is causing this line to be too long."
    )
    _l_(19545)
    exit(aux)

if not string_leaf.parent or [L.type for L in string_leaf.parent.children] == [
    token.STRING,
    token.NEWLINE,
]:
    _l_(19548)

    aux = TErr(
        f"This string ({string_leaf.value}) appears to be pointless (i.e. has"
        " no parent)."
    )
    _l_(19547)
    exit(aux)

if id(line.leaves[string_idx]) in line.comments and contains_pragma_comment(
    line.comments[id(line.leaves[string_idx])]
):
    _l_(19550)

    aux = TErr(
        "Line appears to end with an inline pragma comment. Splitting the line"
        " could modify the pragma's behavior."
    )
    _l_(19549)
    exit(aux)

if has_triple_quotes(string_leaf.value):
    _l_(19552)

    aux = TErr("We cannot split multiline strings.")
    _l_(19551)
    exit(aux)
aux = Ok(None)
_l_(19553)

exit(aux)
