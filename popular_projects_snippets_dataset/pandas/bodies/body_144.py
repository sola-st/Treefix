# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
df = DataFrame({"A": ["foo"], "B": [1.0]})
result = df.apply(lambda x: x["A"], axis=1)
expected = Series(["foo"], index=[0])
tm.assert_series_equal(result, expected)

result = df.apply(lambda x: x["B"], axis=1)
expected = Series([1.0], index=[0])
tm.assert_series_equal(result, expected)
