# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
df = DataFrame({"A": [1, 2], "B": [1, 2]})
result = df.corr(method=method, min_periods=3)
expected = DataFrame(
    {"A": [np.nan, np.nan], "B": [np.nan, np.nan]}, index=["A", "B"]
)
tm.assert_frame_equal(result, expected)
