# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH: 37448
df = DataFrame(length * [[0.4, 0.1]], columns=["A", "B"])
result = df.corr()
expected = DataFrame(
    {"A": [np.nan, np.nan], "B": [np.nan, np.nan]}, index=["A", "B"]
)
tm.assert_frame_equal(result, expected)
