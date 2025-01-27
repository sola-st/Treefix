# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
r1 = pc.convert("2012-1-1", None, axis)
r2 = pc.convert("2012-1-1", None, axis)
assert r1 == r2
