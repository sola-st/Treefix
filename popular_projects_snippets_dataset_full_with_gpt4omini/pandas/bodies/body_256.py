# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py
# GH 19760
df = DataFrame({"A": [-1, 2]})
result = df.transform(method)
expected = operator.methodcaller(method)(df)
tm.assert_frame_equal(result, expected)
