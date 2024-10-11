from typing import List, Callable # pragma: no cover
import token # pragma: no cover

class Leaf: pass # pragma: no cover
class Line: pass # pragma: no cover
line = Line() # pragma: no cover
line.leaves = [Leaf() for _ in range(5)] # pragma: no cover
for i, leaf in enumerate(line.leaves): # pragma: no cover
    leaf.type = token.STRING if i % 2 == 0 else 'OTHER' # pragma: no cover
    leaf.value = 'example string' if leaf.type == token.STRING else 'non-string' # pragma: no cover
def is_valid_index_factory(LL): # pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_valid_index = is_valid_index_factory(line.leaves) # pragma: no cover
def is_part_of_annotation(leaf): return False # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value): self.value = value # pragma: no cover
class TErr: # pragma: no cover
    def __init__(self, message): self.message = message # pragma: no cover

from typing import List, Callable, Any # pragma: no cover
import token # pragma: no cover

class Leaf:  # pragma: no cover
    def __init__(self, type: str, value: str): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
class Line:  # pragma: no cover
    def __init__(self, leaves: List[Leaf]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
line = Line([ # pragma: no cover
    Leaf(token.STRING, 'string1'), # pragma: no cover
    Leaf(token.STRING, 'string2'), # pragma: no cover
    Leaf(token.STRING, 'string\n'), # pragma: no cover
    Leaf('OTHER', 'text'), # pragma: no cover
]) # pragma: no cover
def is_valid_index_factory(LL: List[Leaf]) -> Callable[[int], bool]: # pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_valid_index = is_valid_index_factory(line.leaves) # pragma: no cover
def is_part_of_annotation(leaf: Leaf) -> bool:  # pragma: no cover
    return False # pragma: no cover
def Ok(value: Any): # pragma: no cover
    return {'status': 'OK', 'data': value} # pragma: no cover
def TErr(message: str): # pragma: no cover
    return {'status': 'TErr', 'message': message} # pragma: no cover

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
