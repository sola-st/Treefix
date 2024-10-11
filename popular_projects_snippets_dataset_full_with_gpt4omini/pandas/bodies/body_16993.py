# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
ts = tm.makeTimeSeries()

pieces = [ts[:-2], ts[2:], ts[2:-2]]

result = concat(pieces, axis=1)
expected = DataFrame(pieces).T
tm.assert_frame_equal(result, expected)

result = concat(pieces, keys=["A", "B", "C"], axis=1)
expected = DataFrame(pieces, index=["A", "B", "C"]).T
tm.assert_frame_equal(result, expected)
