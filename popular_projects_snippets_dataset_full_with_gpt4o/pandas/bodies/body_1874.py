# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH39227

if freq == "M":
    request.node.add_marker(pytest.mark.xfail(reason="Don't know why this fails"))

ser = series.copy()
ser.index = PeriodIndex([NaT] * len(ser), freq=freq)
rs = ser.resample(freq)
result = getattr(rs, resample_method)()

if resample_method == "ohlc":
    expected = DataFrame(
        [], index=ser.index[:0].copy(), columns=["open", "high", "low", "close"]
    )
    tm.assert_frame_equal(result, expected, check_dtype=False)
else:
    expected = ser[:0].copy()
    tm.assert_series_equal(result, expected, check_dtype=False)
tm.assert_index_equal(result.index, expected.index)
assert result.index.freq == expected.index.freq
