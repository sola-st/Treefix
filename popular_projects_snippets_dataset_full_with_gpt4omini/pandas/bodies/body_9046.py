# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
msg = "'indices' must be an array, not a scalar '2'."
with pytest.raises(ValueError, match=msg):
    arr.take(2)
