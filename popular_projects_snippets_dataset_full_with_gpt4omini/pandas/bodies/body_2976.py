# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#32995 Don't pass an incorrect axis
pi = date_range("2016-01-01", periods=3).to_period("D")
df = DataFrame({"A": pi})

result = df.diff(1, axis=1)

expected = (df - pd.NaT).astype(object)
tm.assert_frame_equal(result, expected)
