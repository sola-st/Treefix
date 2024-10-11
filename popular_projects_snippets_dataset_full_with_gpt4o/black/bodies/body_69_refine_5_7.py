from typing import List # pragma: no cover
import token # pragma: no cover

line = type('Mock', (object,), {'leaves': [type('Leaf', (object,), {'type': token.STRING, 'value': '"example_string"'})()]}) # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover
is_part_of_annotation = lambda leaf: False # pragma: no cover
Ok = type('Ok', (object,), {'__init__': lambda self, arg: setattr(self, 'value', arg)}) # pragma: no cover
TErr = type('TErr', (object,), {'__init__': lambda self, arg: setattr(self, 'value', arg)}) # pragma: no cover

import token # pragma: no cover
from typing import List, Callable # pragma: no cover
from dataclasses import dataclass # pragma: no cover

# pragma: no cover
 # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    pass
 # pragma: no cover
class TErr: # pragma: no cover
    def __init__(self, message: str): # pragma: no cover
        self.message = message # pragma: no cover
 # pragma: no cover
def TErr(message: str): # pragma: no cover
    print({'status': 'error', 'message': message}) # pragma: no cover

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
