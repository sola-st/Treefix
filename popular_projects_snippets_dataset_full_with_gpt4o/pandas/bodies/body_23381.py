# Extracted from ./data/repos/pandas/pandas/core/interchange/column.py
kind = self.dtype[0]
try:
    null, value = _NULL_DESCRIPTION[kind]
except KeyError:
    raise NotImplementedError(f"Data type {kind} not yet supported")

exit((null, value))
