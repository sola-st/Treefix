# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
assert not isinstance(other, Tick)
raise TypeError(
    f"cannot add the type {type(other).__name__} to a {type(self).__name__}"
)
