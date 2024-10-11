# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#32441
arr = np.arange(6).reshape(3, 2).astype("timedelta64[ns]")
arr[:, 0] = np.timedelta64("NaT", "ns")

df = DataFrame(arr)
result = df.diff(1, axis=0)

expected = DataFrame({0: df[0], 1: [pd.NaT, pd.Timedelta(2), pd.Timedelta(2)]})
tm.assert_equal(result, expected)

result = df.diff(0)
expected = df - df
assert expected[0].isna().all()
tm.assert_equal(result, expected)

result = df.diff(-1, axis=1)
expected = df * np.nan
tm.assert_equal(result, expected)
