from typing import List # pragma: no cover
from dataclasses import dataclass, field # pragma: no cover

@dataclass# pragma: no cover
class MockLeaf:# pragma: no cover
    type: int# pragma: no cover
    value: str = ''# pragma: no cover
# pragma: no cover
@dataclass# pragma: no cover
class MockLine:# pragma: no cover
    leaves: List[MockLeaf] = field(default_factory=list)# pragma: no cover
# pragma: no cover
line = MockLine(leaves=[# pragma: no cover
    MockLeaf(type=1),# pragma: no cover
    MockLeaf(type=3),# pragma: no cover
    MockLeaf(type=1, value='string with \\n'),# pragma: no cover
    MockLeaf(type=3),# pragma: no cover
]) # pragma: no cover
def is_valid_index_factory(leaves: List[MockLeaf]):# pragma: no cover
    def is_valid_index(index: int) -> bool:# pragma: no cover
        return 0 <= index < len(leaves)# pragma: no cover
    return is_valid_index # pragma: no cover
token = type('MockToken', (object,), {'STRING': 1}) # pragma: no cover
def is_part_of_annotation(leaf: MockLeaf) -> bool:# pragma: no cover
    return False # pragma: no cover
def Ok(value):# pragma: no cover
    return f'Ok: {value}'# pragma: no cover
# pragma: no cover
def TErr(error_msg):# pragma: no cover
    return f'Error: {error_msg}' # pragma: no cover

from typing import List, Callable # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type: int, value: str):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self, leaves: List[MockLeaf]):# pragma: no cover
        self.leaves = leaves# pragma: no cover
 # pragma: no cover
line = MockLine(leaves=[# pragma: no cover
    MockLeaf(type=3, value='"string1" '),# pragma: no cover
    MockLeaf(type=3, value='"string2" '),# pragma: no cover
    MockLeaf(type=3, value='"string3" \\n'),# pragma: no cover
    MockLeaf(type=1, value='other'),# pragma: no cover
]) # pragma: no cover
def is_valid_index_factory(leaves: List[MockLeaf]) -> Callable[[int], bool]:# pragma: no cover
    return lambda idx: 0 <= idx < len(leaves) # pragma: no cover
token = type('MockToken', (object,), {'STRING': 3}) # pragma: no cover
def is_part_of_annotation(leaf: MockLeaf) -> bool:# pragma: no cover
    return False # pragma: no cover
class Ok:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'Ok({self.value})' # pragma: no cover
class TErr:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'TErr({self.value})' # pragma: no cover

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
