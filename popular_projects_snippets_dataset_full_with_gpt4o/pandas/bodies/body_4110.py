# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# Both NaT and Timestamp are in DataFrame.
df = DataFrame({"foo": [pd.NaT, pd.NaT, Timestamp("2012-05-01")]})

res = df.min()
exp = Series([Timestamp("2012-05-01")], index=["foo"])
tm.assert_series_equal(res, exp)

res = df.max()
exp = Series([Timestamp("2012-05-01")], index=["foo"])
tm.assert_series_equal(res, exp)

# GH12941, only NaTs are in DataFrame.
df = DataFrame({"foo": [pd.NaT, pd.NaT]})

res = df.min()
exp = Series([pd.NaT], index=["foo"])
tm.assert_series_equal(res, exp)

res = df.max()
exp = Series([pd.NaT], index=["foo"])
tm.assert_series_equal(res, exp)
