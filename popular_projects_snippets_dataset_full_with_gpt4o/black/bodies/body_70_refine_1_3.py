from typing import Union, Any, Dict, Callable # pragma: no cover
from dataclasses import dataclass, InitVar # pragma: no cover

line = 'sample line' # pragma: no cover
string_indices = [0, 5, 10] # pragma: no cover
@dataclass# pragma: no cover
class Ok:# pragma: no cover
    value: Any# pragma: no cover
    def ok(self) -> Any:# pragma: no cover
        return self.value# pragma: no cover
# pragma: no cover
@dataclass# pragma: no cover
class Err:# pragma: no cover
    error: Any# pragma: no cover
    def err(self) -> Any:# pragma: no cover
        return self.error # pragma: no cover
@dataclass# pragma: no cover
class CannotTransform(Exception):# pragma: no cover
    message: str # pragma: no cover
class MockBase:# pragma: no cover
    def _remove_backslash_line_continuation_chars(self, line: str, indices: list) -> Union[Ok, Err]:# pragma: no cover
        # Mock implementation# pragma: no cover
        return Ok(line.replace('\\', ''))# pragma: no cover
# pragma: no cover
    def _merge_string_group(self, line: str, indices: list) -> Union[Ok, Err]:# pragma: no cover
        # Mock implementation# pragma: no cover
        return Ok(line.upper())# pragma: no cover
 # pragma: no cover
self = type('Mock', (MockBase,), {})() # pragma: no cover

from typing import Union, Any # pragma: no cover

line = 'sample line' # pragma: no cover
string_indices = [0, 5, 10] # pragma: no cover
class Ok:# pragma: no cover
    def __init__(self, value: Any):# pragma: no cover
        self._value = value# pragma: no cover
    def ok(self) -> Any:# pragma: no cover
        return self._value# pragma: no cover
 # pragma: no cover
class Err:# pragma: no cover
    def __init__(self, error: Any):# pragma: no cover
        self._error = error# pragma: no cover
    def err(self) -> Any:# pragma: no cover
        return self._error# pragma: no cover
 # pragma: no cover
class CannotTransform(Exception):# pragma: no cover
    def __init__(self, message: str):# pragma: no cover
        self.message = message# pragma: no cover
    def __str__(self):# pragma: no cover
        return self.message# pragma: no cover
 # pragma: no cover
class MockBase:# pragma: no cover
    def _remove_backslash_line_continuation_chars(self, line: str, indices: list) -> Union[Ok, Err]:# pragma: no cover
        # Mock implementation# pragma: no cover
        return Ok(line.replace('\\', ''))# pragma: no cover
# pragma: no cover
    def _merge_string_group(self, line: str, indices: list) -> Union[Ok, Err]:# pragma: no cover
        # Mock implementation# pragma: no cover
        return Ok(line.upper())# pragma: no cover
 # pragma: no cover
self = type('Mock', (MockBase,), {})() # pragma: no cover

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
