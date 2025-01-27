# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH 18421
result_kwargs = self.get_kwargs_from_breaks(breaks)
result = constructor(closed=closed, **result_kwargs)

expected_subtype = np.float64
expected_values = np.array(breaks[:-1], dtype=object)

assert result.closed == closed
assert result.dtype.subtype == expected_subtype
tm.assert_numpy_array_equal(np.array(result), expected_values)
