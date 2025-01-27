# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
with pytest.raises(
    TypeError, match="Cannot construct a 'SparseDtype' from 'not a dtype'"
):
    SparseDtype.construct_from_string("not a dtype")
