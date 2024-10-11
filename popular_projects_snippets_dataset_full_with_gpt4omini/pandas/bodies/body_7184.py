# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
# GH#47475
scalar = np.dtype(any_signed_int_numpy_dtype).type(1)
result = Index([scalar])
expected = Index([1], dtype=any_signed_int_numpy_dtype)
tm.assert_index_equal(result, expected, exact=True)
