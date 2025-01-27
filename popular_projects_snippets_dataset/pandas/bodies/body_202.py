# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 17970
df = DataFrame({"a": [1, 2, 3]}, index=list("abc"))

result = df.apply(lambda row: np.ones(val), axis=1)
expected = Series([np.ones(val) for t in df.itertuples()], index=df.index)
tm.assert_series_equal(result, expected)
