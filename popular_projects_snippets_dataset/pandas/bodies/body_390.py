# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py

# match equal to self, but not equal to other
assert com.is_dtype_equal(dtype1, dtype1)
if name1 != name2:
    assert not com.is_dtype_equal(dtype1, dtype2)
