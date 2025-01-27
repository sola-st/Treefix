# Extracted from ./data/repos/pandas/pandas/tests/strings/test_cat.py
if isinstance(left, Series):
    tm.assert_series_equal(left, right)
else:  # Index
    tm.assert_index_equal(left, right)
