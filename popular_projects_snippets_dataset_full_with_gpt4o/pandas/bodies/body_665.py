# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
expected = arr.astype(float) if coerce else arr.copy()
result, _ = lib.maybe_convert_numeric(arr, set(), coerce_numeric=coerce)
tm.assert_almost_equal(result, expected)
