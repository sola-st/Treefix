# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
subtype, _ = SparseDtype._parse_subtype(string)
assert subtype == expected
