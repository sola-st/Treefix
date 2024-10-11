# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_bool_dtype(int)
assert not com.is_bool_dtype(str)
assert not com.is_bool_dtype(pd.Series([1, 2]))
assert not com.is_bool_dtype(pd.Series(["a", "b"], dtype="category"))
assert not com.is_bool_dtype(np.array(["a", "b"]))
assert not com.is_bool_dtype(pd.Index(["a", "b"]))
assert not com.is_bool_dtype("Int64")

assert com.is_bool_dtype(bool)
assert com.is_bool_dtype(np.bool_)
assert com.is_bool_dtype(pd.Series([True, False], dtype="category"))
assert com.is_bool_dtype(np.array([True, False]))
assert com.is_bool_dtype(pd.Index([True, False]))

assert com.is_bool_dtype(pd.BooleanDtype())
assert com.is_bool_dtype(pd.array([True, False, None], dtype="boolean"))
assert com.is_bool_dtype("boolean")
