# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 16353

df = DataFrame(np.random.randn(6, 3), columns=["A", "B", "C"])

result = df.apply(lambda x: [1, 2, 3], axis=1)
expected = Series([[1, 2, 3] for t in df.itertuples()])
tm.assert_series_equal(result, expected)

result = df.apply(lambda x: [1, 2], axis=1)
expected = Series([[1, 2] for t in df.itertuples()])
tm.assert_series_equal(result, expected)
