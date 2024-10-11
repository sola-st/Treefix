from typing import List, Union # pragma: no cover

line = 'This is an example line.' # pragma: no cover
self = type('Mock', (), { '_remove_backslash_line_continuation_chars': lambda x, y: Ok(), '_merge_string_group': lambda x, y: Ok() })() # pragma: no cover
string_indices = [0, 1, 2] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
new_line = line
_l_(4468)

rblc_result = self._remove_backslash_line_continuation_chars(
    new_line, string_indices
)
_l_(4469)
if isinstance(rblc_result, Ok):
    _l_(4471)

    new_line = rblc_result.ok()
    _l_(4470)

msg_result = self._merge_string_group(new_line, string_indices)
_l_(4472)
if isinstance(msg_result, Ok):
    _l_(4474)

    new_line = msg_result.ok()
    _l_(4473)

if isinstance(rblc_result, Err) and isinstance(msg_result, Err):
    _l_(4482)

    msg_cant_transform = msg_result.err()
    _l_(4475)
    rblc_cant_transform = rblc_result.err()
    _l_(4476)
    cant_transform = CannotTransform(
        "StringMerger failed to merge any strings in this line."
    )
    _l_(4477)

    # Chain the errors together using `__cause__`.
    msg_cant_transform.__cause__ = rblc_cant_transform
    _l_(4478)
    cant_transform.__cause__ = msg_cant_transform
    _l_(4479)
    aux = Err(cant_transform)
    _l_(4480)

    exit(aux)
else:
    aux = Ok(new_line)
    _l_(4481)
    exit(aux)
