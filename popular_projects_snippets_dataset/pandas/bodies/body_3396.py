# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# https://github.com/pandas-dev/pandas/issues/35931
df = DataFrame({"a": [pd.Interval(0, 1), pd.Interval(0, 1)]})
result = df.replace({"a": {pd.Interval(0, 1): "x"}})
expected = DataFrame({"a": ["x", "x"]})
tm.assert_frame_equal(result, expected)
