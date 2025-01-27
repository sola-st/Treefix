# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
base = pd.DatetimeIndex(["2011-01-01", "2011-01-02", "2011-01-03"], tz="UTC")
idx1 = base.tz_convert("Asia/Tokyo")[:2]
idx2 = base.tz_convert("US/Eastern")[1:]

df1 = DataFrame({"A": [1, 2]}, index=idx1)
df2 = DataFrame({"A": [1, 1]}, index=idx2)
exp = DataFrame({"A": [np.nan, 3, np.nan]}, index=base)
tm.assert_frame_equal(df1 + df2, exp)
