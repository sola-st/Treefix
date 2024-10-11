import token # pragma: no cover
from typing import List, Optional # pragma: no cover
from dataclasses import dataclass # pragma: no cover

class MockLeaf:  # Mock class to simulate leaf nodes# pragma: no cover
    def __init__(self, type, value=""):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value # pragma: no cover
def is_valid_index_factory(LL):# pragma: no cover
    def is_valid_index(idx):# pragma: no cover
        return 0 <= idx < len(LL)# pragma: no cover
    return is_valid_index # pragma: no cover
LL = [MockLeaf(token.STRING, 'example string'), MockLeaf(token.STRING, 'another string'), MockLeaf(token.STRING, '\\n'), MockLeaf('OTHER', '')] # pragma: no cover
is_part_of_annotation = lambda leaf: False # pragma: no cover
class Ok:  # Mock class to simulate returning OK# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value # pragma: no cover
class TErr:  # Mock class to simulate returning an error# pragma: no cover
    def __init__(self, message):# pragma: no cover
        self.message = message # pragma: no cover

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
