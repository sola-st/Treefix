# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
rt = ts.asm8
assert rt == dt64
assert rt.dtype == dt64.dtype
