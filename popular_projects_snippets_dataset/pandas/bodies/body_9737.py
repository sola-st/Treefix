# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
# GH 21096
index = date_range(start="2018-1-1 01:00:00", freq=f"1{freq}", periods=10)
# Explicit cast to float to avoid implicit cast when setting nan
s = Series(data=0, index=index, dtype="float")
s.iloc[1] = np.nan
s.iloc[-1] = 2
result = getattr(s.rolling(window=f"10{freq}"), op)()
expected = Series(data=result_data, index=index)

tm.assert_series_equal(result, expected)
