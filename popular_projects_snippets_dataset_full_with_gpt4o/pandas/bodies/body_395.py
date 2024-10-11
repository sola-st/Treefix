# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert com.is_object_dtype(object)
assert com.is_object_dtype(np.array([], dtype=object))

assert not com.is_object_dtype(int)
assert not com.is_object_dtype(np.array([], dtype=int))
assert not com.is_object_dtype([1, 2, 3])
