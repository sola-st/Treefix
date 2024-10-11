from typing import Union # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self._value = value # pragma: no cover
    def ok(self): # pragma: no cover
        return self._value # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error): # pragma: no cover
        self._error = error # pragma: no cover
    def err(self): # pragma: no cover
        return self._error # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover

line = 'some initial value' # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    '_remove_backslash_line_continuation_chars': lambda self, x, y: Ok(x), # pragma: no cover
    '_merge_string_group': lambda self, x, y: Ok(x) # pragma: no cover
})() # pragma: no cover
string_indices = [0, 1, 2] # pragma: no cover
rblc_result = Ok('rblc_result value') # pragma: no cover
msg_result = Ok('msg_result value') # pragma: no cover

class Ok: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self._value = value # pragma: no cover
    def ok(self): # pragma: no cover
        return self._value # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error): # pragma: no cover
        self._error = error # pragma: no cover
    def err(self): # pragma: no cover
        return self._error # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover

line = 'some initial value' # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    '_remove_backslash_line_continuation_chars': lambda self, x, y: Ok(x), # pragma: no cover
    '_merge_string_group': lambda self, x, y: Ok(x) # pragma: no cover
})() # pragma: no cover
string_indices = [0, 1, 2] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
new_line = line
_l_(16150)

rblc_result = self._remove_backslash_line_continuation_chars(
    new_line, string_indices
)
_l_(16151)
if isinstance(rblc_result, Ok):
    _l_(16153)

    new_line = rblc_result.ok()
    _l_(16152)

msg_result = self._merge_string_group(new_line, string_indices)
_l_(16154)
if isinstance(msg_result, Ok):
    _l_(16156)

    new_line = msg_result.ok()
    _l_(16155)

if isinstance(rblc_result, Err) and isinstance(msg_result, Err):
    _l_(16164)

    msg_cant_transform = msg_result.err()
    _l_(16157)
    rblc_cant_transform = rblc_result.err()
    _l_(16158)
    cant_transform = CannotTransform(
        "StringMerger failed to merge any strings in this line."
    )
    _l_(16159)

    # Chain the errors together using `__cause__`.
    msg_cant_transform.__cause__ = rblc_cant_transform
    _l_(16160)
    cant_transform.__cause__ = msg_cant_transform
    _l_(16161)
    aux = Err(cant_transform)
    _l_(16162)

    exit(aux)
else:
    aux = Ok(new_line)
    _l_(16163)
    exit(aux)
