# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py

ts = tm.makeTimeSeries()
ts.name = "foo"

pieces = [ts[:5], ts[5:15], ts[15:]]

result = concat(pieces)
tm.assert_series_equal(result, ts)
assert result.name == ts.name

result = concat(pieces, keys=[0, 1, 2])
expected = ts.copy()

ts.index = DatetimeIndex(np.array(ts.index.values, dtype="M8[ns]"))

exp_codes = [np.repeat([0, 1, 2], [len(x) for x in pieces]), np.arange(len(ts))]
exp_index = MultiIndex(levels=[[0, 1, 2], ts.index], codes=exp_codes)
expected.index = exp_index
tm.assert_series_equal(result, expected)
