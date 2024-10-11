# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH 18421
result_kwargs = self.get_kwargs_from_breaks(breaks)
result = constructor(closed=closed, **result_kwargs)

expected_values = np.array([], dtype=object)
expected_subtype = getattr(breaks, "dtype", np.int64)

assert result.empty
assert result.closed == closed
assert result.dtype.subtype == expected_subtype
tm.assert_numpy_array_equal(np.array(result), expected_values)
