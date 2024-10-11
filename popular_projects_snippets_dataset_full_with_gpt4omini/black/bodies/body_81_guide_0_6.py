from typing import List, Optional, Union # pragma: no cover
import token # pragma: no cover

class TErr(Exception): pass # pragma: no cover

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
_l_(8041)

string_leaf = LL[string_idx]
_l_(8042)

max_string_length = self._get_max_string_length(line, string_idx)
_l_(8043)
if len(string_leaf.value) <= max_string_length:
    _l_(8045)

    aux = TErr(
        "The string itself is not what is causing this line to be too long."
    )
    _l_(8044)
    exit(aux)

if not string_leaf.parent or [L.type for L in string_leaf.parent.children] == [
    token.STRING,
    token.NEWLINE,
]:
    _l_(8047)

    aux = TErr(
        f"This string ({string_leaf.value}) appears to be pointless (i.e. has"
        " no parent)."
    )
    _l_(8046)
    exit(aux)

if id(line.leaves[string_idx]) in line.comments and contains_pragma_comment(
    line.comments[id(line.leaves[string_idx])]
):
    _l_(8049)

    aux = TErr(
        "Line appears to end with an inline pragma comment. Splitting the line"
        " could modify the pragma's behavior."
    )
    _l_(8048)
    exit(aux)

if has_triple_quotes(string_leaf.value):
    _l_(8051)

    aux = TErr("We cannot split multiline strings.")
    _l_(8050)
    exit(aux)
aux = Ok(None)
_l_(8052)

exit(aux)
