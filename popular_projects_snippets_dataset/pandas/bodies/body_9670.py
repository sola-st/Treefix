# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_astype.py
arr = period_array(["2000", "2001", None], freq="D")
result = arr.astype(np.int64, copy=False)

# Add the `.base`, since we now use `.asi8` which returns a view.
# We could maybe override it in PeriodArray to return ._ndarray directly.
assert result.base is arr._ndarray

result = arr.astype(np.int64, copy=True)
assert result is not arr._ndarray
tm.assert_numpy_array_equal(result, arr._ndarray.view("i8"))
