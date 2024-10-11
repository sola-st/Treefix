# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 39111
df = DataFrame({"a": [1, 2], "b": [3, 0]})
result = df.head(0).apply(lambda x: max(x["a"], x["b"]), axis=1)
expected = Series([], dtype=np.float64)
tm.assert_series_equal(result, expected)
