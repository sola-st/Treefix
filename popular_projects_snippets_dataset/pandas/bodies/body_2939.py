# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dtypes.py
# GH 35517
df = DataFrame([["foo"]])
result = df.apply(lambda col: np.array("bar"))
expected = Series(["bar"])
tm.assert_series_equal(result, expected)
