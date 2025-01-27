# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
result = SparseArray(data).fill_value

if isna(fill_value):
    assert isna(result)
else:
    assert result == fill_value
