class Ok: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self._value = value # pragma: no cover
    def ok(self): return self._value # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error): # pragma: no cover
        self._error = error # pragma: no cover
    def err(self): return self._error # pragma: no cover
class CannotTransform(Exception): pass # pragma: no cover

line = 'sample line with \ continuation' # pragma: no cover
string_indices = [] # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_remove_backslash_line_continuation_chars': lambda self, line, indices: Err('Error removing backslash'), # pragma: no cover
    '_merge_string_group': lambda self, line, indices: Err('Error merging strings') # pragma: no cover
})() # pragma: no cover

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
