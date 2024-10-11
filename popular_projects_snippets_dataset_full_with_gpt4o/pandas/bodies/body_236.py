# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# https://github.com/pandas-dev/pandas/issues/35940
df = DataFrame({"A": ["aa", "bbb"]})
result = df.apply(lambda x: x[0], axis=1, raw=True)
expected = Series(["aa", "bbb"])
tm.assert_series_equal(result, expected)
