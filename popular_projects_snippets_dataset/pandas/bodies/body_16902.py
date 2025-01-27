# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
# see gh-19891
ser = Series(arg)
result, result_bins = qcut(ser, 2, retbins=True)
tm.assert_index_equal(result_bins, expected_bins)
