# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
left = _get_offset("ms")
right = _get_offset("MS")

assert left == offsets.Milli()
assert right == offsets.MonthBegin()
