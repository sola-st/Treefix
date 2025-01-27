# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#46947
df = DataFrame({"a": [1.0, 2.3, 4.4], "b": [2.2, 3, np.nan]}, dtype=float_type)
result = df.sum(**kwargs)
expected = Series(expected_result).astype(float_type)
tm.assert_series_equal(result, expected)
