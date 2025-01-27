# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 13427
df = DataFrame({"a": [0, 1, 2], "b": [1, 2, 3]})
result = df[["a", "a"]].apply(lambda x: x[0] + x[1], axis=1)
expected = Series([0, 2, 4])
tm.assert_series_equal(result, expected)
