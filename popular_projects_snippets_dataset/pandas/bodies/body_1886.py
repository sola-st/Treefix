# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# test for fill value during resampling, issue 3715

s = series
new_index = date_range(
    s.index[0].to_timestamp(how="start"),
    (s.index[-1]).to_timestamp(how="start"),
    freq="1H",
)
expected = s.to_timestamp().reindex(new_index, fill_value=4.0)
result = s.resample("1H", kind="timestamp").asfreq(fill_value=4.0)
tm.assert_series_equal(result, expected)

frame = s.to_frame("value")
new_index = date_range(
    frame.index[0].to_timestamp(how="start"),
    (frame.index[-1]).to_timestamp(how="start"),
    freq="1H",
)
expected = frame.to_timestamp().reindex(new_index, fill_value=3.0)
result = frame.resample("1H", kind="timestamp").asfreq(fill_value=3.0)
tm.assert_frame_equal(result, expected)
