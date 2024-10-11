# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
result = getattr(s, op_name)(skipna=skipna)
# avoid coercing int -> float. Just cast to the actual numpy type.
expected = getattr(s.astype(s.dtype._dtype), op_name)(skipna=skipna)
tm.assert_almost_equal(result, expected)
