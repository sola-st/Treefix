# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# https://github.com/pandas-dev/pandas/issues/48656
df = DataFrame({"A": [1, 2, 0], "B": [0, 2, 0], "C": [0, 0, 0]})
expected = Series([True, True, False])
tm.assert_series_equal(df.any(axis=1), expected)

result = df.apply("any", axis=1)
tm.assert_series_equal(result, expected)

result = df.apply("any", 1)
tm.assert_series_equal(result, expected)
