# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# test for fill value during resampling, issue 3715

ser = series

result = ser.resample("1H").asfreq()
new_index = create_index(ser.index[0], ser.index[-1], freq="1H")
expected = ser.reindex(new_index)
tm.assert_series_equal(result, expected)

# Explicit cast to float to avoid implicit cast when setting None
frame = ser.astype("float").to_frame("value")
frame.iloc[1] = None
result = frame.resample("1H").asfreq(fill_value=4.0)
new_index = create_index(frame.index[0], frame.index[-1], freq="1H")
expected = frame.reindex(new_index, fill_value=4.0)
tm.assert_frame_equal(result, expected)
