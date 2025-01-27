# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
ser = Series([1.0, np.nan], index=[0, 1])
result = np.nansum(ser)
tm.assert_almost_equal(result, 1)
