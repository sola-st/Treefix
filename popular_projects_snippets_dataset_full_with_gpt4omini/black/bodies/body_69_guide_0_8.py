import token # pragma: no cover
from typing import List # pragma: no cover
import dataclasses # pragma: no cover

class Leaf: pass # pragma: no cover
class Line: pass # pragma: no cover
def is_valid_index_factory(LL: List[Leaf]) -> callable: return lambda idx: 0 <= idx < len(LL) # pragma: no cover
def is_part_of_annotation(leaf: Leaf) -> bool: return False # pragma: no cover
line = Line() # pragma: no cover
line.leaves = [Leaf(), Leaf(), Leaf()] # pragma: no cover
line.leaves[0].type = token.STRING # pragma: no cover
line.leaves[0].value = 'Hello' # pragma: no cover
line.leaves[1].type = token.STRING # pragma: no cover
line.leaves[1].value = 'World' # pragma: no cover
line.leaves[2].type = token.STRING # pragma: no cover
line.leaves[2].value = '\n' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(7829)

is_valid_index = is_valid_index_factory(LL)
_l_(7830)

string_indices = []
_l_(7831)
idx = 0
_l_(7832)
while is_valid_index(idx):
    _l_(7846)

    leaf = LL[idx]
    _l_(7833)
    if (
        leaf.type == token.STRING
        and is_valid_index(idx + 1)
        and LL[idx + 1].type == token.STRING
    ):
        _l_(7845)

        if not is_part_of_annotation(leaf):
            _l_(7835)

            string_indices.append(idx)
            _l_(7834)

        # Advance to the next non-STRING leaf.
        idx += 2
        _l_(7836)
        while is_valid_index(idx) and LL[idx].type == token.STRING:
            _l_(7838)

            idx += 1
            _l_(7837)

    elif leaf.type == token.STRING and "\\\n" in leaf.value:
        _l_(7844)

        string_indices.append(idx)
        _l_(7839)
        # Advance to the next non-STRING leaf.
        idx += 1
        _l_(7840)
        while is_valid_index(idx) and LL[idx].type == token.STRING:
            _l_(7842)

            idx += 1
            _l_(7841)

    else:
        idx += 1
        _l_(7843)

if string_indices:
    _l_(7849)

    aux = Ok(string_indices)
    _l_(7847)
    exit(aux)
else:
    aux = TErr("This line has no strings that need merging.")
    _l_(7848)
    exit(aux)
