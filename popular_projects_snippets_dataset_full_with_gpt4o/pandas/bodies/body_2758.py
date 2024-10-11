# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_and_last.py
ts = tm.makeTimeDataFrame(freq="12h")
ts = tm.get_obj(ts, frame_or_series)
result = ts.last("10d")
assert len(result) == 20

ts = tm.makeTimeDataFrame(nper=30, freq="D")
ts = tm.get_obj(ts, frame_or_series)
result = ts.last("10d")
assert len(result) == 10

result = ts.last("21D")
expected = ts["2000-01-10":]
tm.assert_equal(result, expected)

result = ts.last("21D")
expected = ts[-21:]
tm.assert_equal(result, expected)

result = ts[:0].last("3M")
tm.assert_equal(result, ts[:0])
