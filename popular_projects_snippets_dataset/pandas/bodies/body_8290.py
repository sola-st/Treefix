# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_frame.py
# GH#25809
idx = date_range(start="2019-01-01", end="2019-01-30", freq="D", tz="UTC")
result = idx.to_frame()
expected = DataFrame(idx, index=idx)
tm.assert_frame_equal(result, expected)
