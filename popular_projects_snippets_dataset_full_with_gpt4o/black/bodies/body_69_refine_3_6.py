from typing import List, Union, Callable # pragma: no cover
from dataclasses import dataclass, field # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    type: int # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Leaf] = field(default_factory=list) # pragma: no cover
 # pragma: no cover
line = Line(leaves=[Leaf(type=1, value='dummy_value')]) # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves: List[Leaf]) -> Callable[[int], bool]: # pragma: no cover
    return lambda idx: 0 <= idx < len(leaves) # pragma: no cover
 # pragma: no cover
token = type('MockToken', (object,), {'STRING': 1}) # pragma: no cover
 # pragma: no cover
def is_part_of_annotation(leaf: Leaf) -> bool: # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def Ok(value: Union[str, List[int]]) -> dict: # pragma: no cover
    return {'status': 'ok', 'result': value} # pragma: no cover
 # pragma: no cover
def TErr(message: str) -> dict: # pragma: no cover
    return {'status': 'error', 'message': message} # pragma: no cover

from typing import List, Callable # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    type: int # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Leaf] # pragma: no cover
 # pragma: no cover
line = Line(leaves=[ # pragma: no cover
    Leaf(type=3, value='"string1"'), # pragma: no cover
    Leaf(type=3, value='"string2"'), # pragma: no cover
    Leaf(type=3, value='"string3"'), # pragma: no cover
    Leaf(type=1, value='non-string') # pragma: no cover
]) # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves: List[Leaf]) -> Callable[[int], bool]: # pragma: no cover
    def is_valid_index(idx: int) -> bool: # pragma: no cover
        return 0 <= idx < len(leaves) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
class token: # pragma: no cover
    STRING = 3 # pragma: no cover
 # pragma: no cover
def is_part_of_annotation(leaf: Leaf) -> bool: # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def Ok(value): # pragma: no cover
    print(value) # pragma: no cover
    return {'status': 'ok', 'result': value} # pragma: no cover
 # pragma: no cover
def TErr(message: str): # pragma: no cover
    print(message) # pragma: no cover
    return {'status': 'error', 'message': message} # pragma: no cover

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
