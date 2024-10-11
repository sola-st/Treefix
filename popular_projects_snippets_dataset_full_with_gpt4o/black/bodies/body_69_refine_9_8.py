from typing import List, Union # pragma: no cover
from dataclasses import dataclass # pragma: no cover
import token # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    type: int # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Leaf] # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(LL: List[Leaf]): # pragma: no cover
    return lambda index: 0 <= index < len(LL) # pragma: no cover
 # pragma: no cover
def is_part_of_annotation(leaf: Leaf) -> bool: # pragma: no cover
    # Mock implementation, assume no leaf is part of an annotation # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
def Ok(value: List[int]) -> str: # pragma: no cover
    return f"Ok: {value}" # pragma: no cover
 # pragma: no cover
def TErr(message: str) -> str: # pragma: no cover
    return f"Error: {message}" # pragma: no cover

from typing import List, Callable # pragma: no cover
import token # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type: int, value: str): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self, leaves: List[Leaf]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
line = Line(leaves=[Leaf(type=token.STRING, value='"hello"'), Leaf(type=token.STRING, value='"world"'), Leaf(type=1, value='non-string')]) # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves: List[Leaf]) -> Callable[[int], bool]: # pragma: no cover
    def is_valid_index(index: int) -> bool: # pragma: no cover
        return 0 <= index < len(leaves) # pragma: no cover
    return is_valid_index # pragma: no cover
 # pragma: no cover
def is_part_of_annotation(leaf: Leaf) -> bool: # pragma: no cover
    return False # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
    def __repr__(self): # pragma: no cover
        return f'Ok({self.value})' # pragma: no cover
 # pragma: no cover
class TErr: # pragma: no cover
    def __init__(self, message): # pragma: no cover
        self.message = message # pragma: no cover
    def __repr__(self): # pragma: no cover
        return f'TErr({self.message})' # pragma: no cover

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
