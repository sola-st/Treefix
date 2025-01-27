# Extracted from ./data/repos/pandas/pandas/tests/series/test_cumulative.py
# with ts==pd.Timedelta(0), we are testing td64; with naive Timestamp
#  we are testing datetime64[ns]; with Timestamp[US/Pacific]
#  we are testing dt64tz
tdi = pd.to_timedelta(["NaT", "2 days", "NaT", "1 days", "NaT", "3 days"])
ser = pd.Series(tdi + ts)

exp_tdi = pd.to_timedelta(exp_tdi)
expected = pd.Series(exp_tdi + ts)
result = getattr(ser, method)(skipna=skipna)
tm.assert_series_equal(expected, result)
