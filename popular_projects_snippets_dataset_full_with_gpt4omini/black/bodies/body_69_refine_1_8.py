from typing import List, Callable, Any, Union # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type: str, value: str):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value # pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self, leaves: List[MockLeaf]):# pragma: no cover
        self.leaves = leaves # pragma: no cover
def is_valid_index_factory(LL: List[MockLeaf]) -> Callable[[int], bool]:# pragma: no cover
    def is_valid_index(idx: int) -> bool:# pragma: no cover
        return 0 <= idx < len(LL)# pragma: no cover
    return is_valid_index # pragma: no cover
class MockToken:# pragma: no cover
    STRING = 'STRING' # pragma: no cover
def is_part_of_annotation(leaf: MockLeaf) -> bool:# pragma: no cover
    return False # pragma: no cover
class Ok:# pragma: no cover
    def __init__(self, value: Any):# pragma: no cover
        self.value = value# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'Ok({self.value})' # pragma: no cover
class TErr:# pragma: no cover
    def __init__(self, message: str):# pragma: no cover
        self.message = message# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'TErr({self.message})' # pragma: no cover
line = MockLine([MockLeaf('STRING', 'example1'), MockLeaf('STRING', 'example2'), MockLeaf('STRING', 'example\n'), MockLeaf('OTHER', 'text')]) # pragma: no cover
token = MockToken() # pragma: no cover

from typing import List, Callable, Any # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type: str, value: str):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value # pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self, leaves: List[MockLeaf]):# pragma: no cover
        self.leaves = leaves # pragma: no cover
def is_valid_index_factory(LL: List[MockLeaf]) -> Callable[[int], bool]:# pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
class MockToken:# pragma: no cover
    STRING = 'STRING' # pragma: no cover
def is_part_of_annotation(leaf: MockLeaf) -> bool:# pragma: no cover
    return False # pragma: no cover
class Ok:# pragma: no cover
    def __init__(self, value: Any):# pragma: no cover
        self.value = value# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'OK: {self.value}' # pragma: no cover
class TErr:# pragma: no cover
    def __init__(self, message: str):# pragma: no cover
        self.message = message# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'TE: {self.message}' # pragma: no cover
line = MockLine([MockLeaf('STRING', 'example string'), MockLeaf('STRING', 'another string'), MockLeaf('STRING', 'multiline\ntext'), MockLeaf('OTHER', 'not a string')]) # pragma: no cover
token = MockToken() # pragma: no cover

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
