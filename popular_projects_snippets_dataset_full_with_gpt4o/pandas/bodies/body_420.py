# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_datetime64_any_dtype(int)
assert not com.is_datetime64_any_dtype(str)
assert not com.is_datetime64_any_dtype(np.array([1, 2]))
assert not com.is_datetime64_any_dtype(np.array(["a", "b"]))

assert com.is_datetime64_any_dtype(np.datetime64)
assert com.is_datetime64_any_dtype(np.array([], dtype=np.datetime64))
assert com.is_datetime64_any_dtype(DatetimeTZDtype("ns", "US/Eastern"))
assert com.is_datetime64_any_dtype(
    pd.DatetimeIndex([1, 2, 3], dtype="datetime64[ns]")
)
