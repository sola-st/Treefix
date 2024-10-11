# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
result = Series(array, dtype=dtype).mode()
tm.assert_series_equal(result, expected)
