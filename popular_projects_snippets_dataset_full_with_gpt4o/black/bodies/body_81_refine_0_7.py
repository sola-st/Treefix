from typing import List, Optional, Dict # pragma: no cover
from typing_extensions import Literal # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass# pragma: no cover
class Leaf:# pragma: no cover
    value: str# pragma: no cover
    parent: Optional['Leaf']# pragma: no cover
    children: List['Leaf']# pragma: no cover
    type: Optional[str] = None# pragma: no cover
# pragma: no cover
@dataclass# pragma: no cover
class Comment:# pragma: no cover
    content: str# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
line = Mock()# pragma: no cover
line.leaves = [# pragma: no cover
    Leaf(value='short string', parent=None, children=[]),# pragma: no cover
    Leaf(value='valid string', parent=None, children=[])# pragma: no cover
]# pragma: no cover
line.comments = {}# pragma: no cover
string_idx = 1# pragma: no cover
# pragma: no cover
self = Mock()# pragma: no cover
self._get_max_string_length = lambda line, idx: 15# pragma: no cover
# pragma: no cover
TErr = lambda msg: f'Error: {msg}'# pragma: no cover
token = Mock()# pragma: no cover
token.STRING = 'STRING'# pragma: no cover
token.NEWLINE = 'NEWLINE'# pragma: no cover
# pragma: no cover
def contains_pragma_comment(comment):# pragma: no cover
    return 'pragma' in comment.content# pragma: no cover
# pragma: no cover
def has_triple_quotes(string_val):# pragma: no cover
    return '"""' in string_val or "'''" in string_val# pragma: no cover
# pragma: no cover
Ok = lambda x: f'Ok: {x}'# pragma: no cover
 # pragma: no cover

from typing import List, Optional, Dict # pragma: no cover
from typing_extensions import Literal # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass# pragma: no cover
class Leaf:# pragma: no cover
    value: str# pragma: no cover
    parent: Optional['Leaf']# pragma: no cover
    children: List['Leaf']# pragma: no cover
    type: Optional[str] = None# pragma: no cover
# pragma: no cover
@dataclass# pragma: no cover
class Comment:# pragma: no cover
    content: str# pragma: no cover
# pragma: no cover
class Mock:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
line = Mock()# pragma: no cover
line.leaves = [# pragma: no cover
    Leaf(value='short string', parent=None, children=[]),# pragma: no cover
    Leaf(value='valid string exceeding max length', parent=None, children=[])# pragma: no cover
]# pragma: no cover
line.comments = {}# pragma: no cover
string_idx = 1# pragma: no cover
# pragma: no cover
self = Mock()# pragma: no cover
self._get_max_string_length = lambda line, idx: 15# pragma: no cover
# pragma: no cover
TErr = lambda msg: f'Error: {msg}'# pragma: no cover
token = Mock()# pragma: no cover
token.STRING = 'STRING'# pragma: no cover
token.NEWLINE = 'NEWLINE'# pragma: no cover
# pragma: no cover
def contains_pragma_comment(comment):# pragma: no cover
    return 'pragma' in comment.content# pragma: no cover
# pragma: no cover
def has_triple_quotes(string_val):# pragma: no cover
    return '"""' in string_val or "'''" in string_val# pragma: no cover
# pragma: no cover
Ok = lambda x: f'Ok: {x}'# pragma: no cover
 # pragma: no cover

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
