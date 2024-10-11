# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_repr.py
# smoke tests on auto dtype construction

np.dtype(dtype.type).kind == "f"
assert dtype.name is not None
