# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
val = -val if signed else val
assert to_numeric(transform(val)) == float(val)
