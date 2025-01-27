# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
with pytest.raises(TypeError, match="fill_value in the string is not"):
    SparseDtype.construct_from_string(string)
