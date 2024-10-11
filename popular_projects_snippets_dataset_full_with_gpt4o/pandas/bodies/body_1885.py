# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH 12884, 15944
# make sure .asfreq() returns PeriodIndex (except kind='timestamp')

obj = series_and_frame
if kind == "timestamp":
    expected = obj.to_timestamp().resample(freq).asfreq()
else:
    start = obj.index[0].to_timestamp(how="start")
    end = (obj.index[-1] + obj.index.freq).to_timestamp(how="start")
    new_index = date_range(start=start, end=end, freq=freq, inclusive="left")
    expected = obj.to_timestamp().reindex(new_index).to_period(freq)
result = obj.resample(freq, kind=kind).asfreq()
tm.assert_almost_equal(result, expected)
