# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_pct_change.py
# GH#28664
common_idx = date_range("2019-11-14", periods=5, freq="D")
result = Series(range(5), common_idx).pct_change(freq="B")

# the reason that the expected should be like this is documented at PR 28681
expected = Series([np.NaN, np.inf, np.NaN, np.NaN, 3.0], common_idx)

tm.assert_series_equal(result, expected)
