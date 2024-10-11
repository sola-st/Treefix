from tokenize import STRING # pragma: no cover
from typing import List, Any # pragma: no cover

class MockLeaf: # pragma: no cover
    type: int # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
line = type('Mock', (object,), {'leaves': [MockLeaf() for _ in range(3)]})() # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(LL: List[Any]): # pragma: no cover
    def is_valid_index(index: int) -> bool: # pragma: no cover
        return 0 <= index < len(LL) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
def is_part_of_annotation(leaf: Any) -> bool: # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
class MockToken: # pragma: no cover
    STRING = STRING # pragma: no cover
 # pragma: no cover
token = MockToken() # pragma: no cover
 # pragma: no cover
line.leaves[0].type = token.STRING # pragma: no cover
line.leaves[0].value = '"string1"\\\n' # pragma: no cover
line.leaves[1].type = token.STRING # pragma: no cover
line.leaves[1].value = '"string2"' # pragma: no cover
line.leaves[2].type = token.STRING # pragma: no cover
line.leaves[2].value = '"string3"' # pragma: no cover

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
