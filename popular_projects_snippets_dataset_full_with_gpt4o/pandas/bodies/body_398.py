# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_datetime64_dtype(object)
assert not com.is_datetime64_dtype([1, 2, 3])
assert not com.is_datetime64_dtype(np.array([], dtype=int))

assert com.is_datetime64_dtype(np.datetime64)
assert com.is_datetime64_dtype(np.array([], dtype=np.datetime64))
