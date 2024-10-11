from typing import List, Callable # pragma: no cover
import token # pragma: no cover

class MockLineLeaf: # pragma: no cover
    def __init__(self, type, value=''): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves: List[MockLineLeaf]) -> Callable[[int], bool]: # pragma: no cover
    return lambda idx: 0 <= idx < len(leaves) # pragma: no cover
 # pragma: no cover
def is_part_of_annotation(leaf: MockLineLeaf) -> bool: # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
line = type('MockLine', (object,), {'leaves': [MockLineLeaf(token.STRING, '"hello""world"'), MockLineLeaf(token.STRING, '"continuing"') ]}) # pragma: no cover
 # pragma: no cover
Ok = lambda x: x # pragma: no cover
TErr = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(19308)

is_valid_index = is_valid_index_factory(LL)
_l_(19309)

string_indices = []
_l_(19310)
idx = 0
_l_(19311)
while is_valid_index(idx):
    _l_(19325)

    leaf = LL[idx]
    _l_(19312)
    if (
        leaf.type == token.STRING
        and is_valid_index(idx + 1)
        and LL[idx + 1].type == token.STRING
    ):
        _l_(19324)

        if not is_part_of_annotation(leaf):
            _l_(19314)

            string_indices.append(idx)
            _l_(19313)

        # Advance to the next non-STRING leaf.
        idx += 2
        _l_(19315)
        while is_valid_index(idx) and LL[idx].type == token.STRING:
            _l_(19317)

            idx += 1
            _l_(19316)

    elif leaf.type == token.STRING and "\\\n" in leaf.value:
        _l_(19323)

        string_indices.append(idx)
        _l_(19318)
        # Advance to the next non-STRING leaf.
        idx += 1
        _l_(19319)
        while is_valid_index(idx) and LL[idx].type == token.STRING:
            _l_(19321)

            idx += 1
            _l_(19320)

    else:
        idx += 1
        _l_(19322)

if string_indices:
    _l_(19328)

    aux = Ok(string_indices)
    _l_(19326)
    exit(aux)
else:
    aux = TErr("This line has no strings that need merging.")
    _l_(19327)
    exit(aux)
