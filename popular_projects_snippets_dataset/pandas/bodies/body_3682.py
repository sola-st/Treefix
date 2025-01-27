# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
# GH#15473
df1_ts = DataFrame({"date": pd.to_datetime(["2014-01-01", "2014-01-02"])})
df1_td = DataFrame({"date": [pd.Timedelta(1, "s"), pd.Timedelta(2, "s")]})
df2 = DataFrame({"date": []})
df3 = DataFrame()

expected = DataFrame({"date": [False, False]})

result = df1_ts.isin(df2)
tm.assert_frame_equal(result, expected)
result = df1_ts.isin(df3)
tm.assert_frame_equal(result, expected)

result = df1_td.isin(df2)
tm.assert_frame_equal(result, expected)
result = df1_td.isin(df3)
tm.assert_frame_equal(result, expected)
