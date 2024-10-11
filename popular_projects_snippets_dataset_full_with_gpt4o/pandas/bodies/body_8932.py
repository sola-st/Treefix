# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
left = SparseArray([True, True])
right = cons([True, True, True])
with pytest.raises(ValueError, match="operands have mismatched length"):
    left & right
