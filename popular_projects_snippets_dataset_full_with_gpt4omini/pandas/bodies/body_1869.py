# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
obj = series_and_frame

result = obj.resample(freq).asfreq()
new_index = create_index(obj.index[0], obj.index[-1], freq=freq)
expected = obj.reindex(new_index)
tm.assert_almost_equal(result, expected)
