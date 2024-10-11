# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# we want column names to NOT be propagated
# just because the shape matches the input shape
df = DataFrame(np.random.randn(4, 3), columns=["A", "B", "C"])

result = df.apply(lambda x: lst, axis=1)
expected = Series([lst for t in df.itertuples()])
tm.assert_series_equal(result, expected)
