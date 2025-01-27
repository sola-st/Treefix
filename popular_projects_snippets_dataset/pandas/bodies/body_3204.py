# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
# GH#14320
index = DatetimeIndex(["2016-09-29 11:00"])
expected = frame_or_series(index=index, dtype=object).asfreq("H")
result = frame_or_series([3], index=index.copy()).asfreq("H")
tm.assert_index_equal(expected.index, result.index)
