from typing import List, Dict, Any # pragma: no cover
from collections import namedtuple # pragma: no cover
import token # pragma: no cover

line = type('MockLine', (object,), {'leaves': [], 'comments': {}})() # pragma: no cover
string_idx = 0 # pragma: no cover
self = type('MockSelf', (object,), {'_get_max_string_length': lambda self, line, idx: 10})() # pragma: no cover
TErr = namedtuple('TErr', ['message']) # pragma: no cover
token = type('MockToken', (object,), {'STRING': 3, 'NEWLINE': 4}) # pragma: no cover
contains_pragma_comment = lambda comment: False # pragma: no cover
has_triple_quotes = lambda s: False # pragma: no cover
Ok = lambda x: namedtuple('Ok', ['value'])(x) # pragma: no cover

from typing import List, Optional # pragma: no cover
import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, value: str, parent: Optional['Leaf'] = None, children: Optional[List['Leaf']] = None):# pragma: no cover
        if children is None:# pragma: no cover
            children = []# pragma: no cover
        self.value = value# pragma: no cover
        self.parent = parent# pragma: no cover
        self.children = children# pragma: no cover
        self.type = token.STRING # pragma: no cover
line = type('MockLine', (object,), {'leaves': [Leaf('short string'), Leaf('valid string')], 'comments': {}})() # pragma: no cover
string_idx = 1 # pragma: no cover
self = type('MockSelf', (object,), {'_get_max_string_length': lambda self, line, idx: 15})() # pragma: no cover
TErr = lambda msg: f'Error: {msg}' # pragma: no cover
contains_pragma_comment = lambda comment: False # pragma: no cover
has_triple_quotes = lambda s: False # pragma: no cover
Ok = lambda x: f'Ok: {x}' # pragma: no cover

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
