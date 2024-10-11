from typing import NamedTuple, List # pragma: no cover
from mypy_extensions import TypedDict # pragma: no cover

class Line(NamedTuple): # pragma: no cover
    leaves: List # pragma: no cover
    comments: dict # pragma: no cover
 # pragma: no cover
class MockSelf(NamedTuple): # pragma: no cover
    def _get_max_string_length(self, line, string_idx): # pragma: no cover
        return 80 # pragma: no cover
 # pragma: no cover
class Token(TypedDict): # pragma: no cover
    STRING: int # pragma: no cover
    NEWLINE: int # pragma: no cover
 # pragma: no cover
def contains_pragma_comment(comment): # pragma: no cover
    # Example implementation # pragma: no cover
    return 'pragma' in comment # pragma: no cover
 # pragma: no cover
def has_triple_quotes(value): # pragma: no cover
    # Example implementation # pragma: no cover
    return '"""' in value or "'''" in value # pragma: no cover
 # pragma: no cover
def Ok(value): # pragma: no cover
    return ('Ok', value) # pragma: no cover
 # pragma: no cover
def TErr(message): # pragma: no cover
    return ('Err', message) # pragma: no cover
 # pragma: no cover
line = Line(leaves=[type('Leaf', (object,), {'value': 'example', 'parent': None})], comments={}) # pragma: no cover
string_idx = 0 # pragma: no cover
self = MockSelf() # pragma: no cover
token = Token(STRING=1, NEWLINE=2) # pragma: no cover

from typing import List, Optional # pragma: no cover
import token # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, value: str, parent: Optional['Leaf'] = None): # pragma: no cover
        self.value = value # pragma: no cover
        self.parent = parent # pragma: no cover
        self.children = [] # pragma: no cover
        self.type = None # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [Leaf('a very long example string that exceeds the maximum length')] # pragma: no cover
        self.comments = {} # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def _get_max_string_length(self, line, string_idx): # pragma: no cover
        return 20 # pragma: no cover
 # pragma: no cover
def contains_pragma_comment(comment): # pragma: no cover
    return 'pragma' in comment # pragma: no cover
 # pragma: no cover
def has_triple_quotes(string_val): # pragma: no cover
    return '"""' in string_val or "'''" in string_val # pragma: no cover
 # pragma: no cover
def Ok(x): # pragma: no cover
    return f'Ok: {x}' # pragma: no cover
 # pragma: no cover
def TErr(msg): # pragma: no cover
    return f'Err: {msg}' # pragma: no cover
 # pragma: no cover
line = MockLine() # pragma: no cover
string_idx = 0 # pragma: no cover
self = MockSelf() # pragma: no cover

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
