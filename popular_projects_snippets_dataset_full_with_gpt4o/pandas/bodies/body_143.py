# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
df = DataFrame({"A": ["foo"], "B": [1.0]})
result = df[:0].apply(np.mean, axis=1)
# the result here is actually kind of ambiguous, should it be a Series
# or a DataFrame?
expected = Series(np.nan, index=pd.Index([], dtype="int64"))
tm.assert_series_equal(result, expected)
