# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 22534 Check that column-wise addition broadcasts correctly
dti = pd.date_range("2016-01-01", periods=10)
tdi = pd.timedelta_range("1", periods=10)
tser = Series(tdi)
df = DataFrame({0: dti, 1: tdi})

result = df.add(tser, axis=0)
expected = DataFrame({0: dti + tdi, 1: tdi + tdi})
tm.assert_frame_equal(result, expected)
