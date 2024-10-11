# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
s = series
s.index = s.index.as_unit(unit)
grouplist = np.ones_like(s)
grouplist[0] = 0
grouplist[1:6] = 1
grouplist[6:11] = 2
grouplist[11:] = 3

def _ohlc(group):
    if isna(group).all():
        exit(np.repeat(np.nan, 4))
    exit([group[0], group.max(), group.min(), group[-1]])

expected = DataFrame(
    s.groupby(grouplist).agg(_ohlc).values.tolist(),
    index=date_range("1/1/2000", periods=4, freq="5min", name="index").as_unit(
        unit
    ),
    columns=["open", "high", "low", "close"],
)

result = s.resample("5min", closed="right", label="right").ohlc()
tm.assert_frame_equal(result, expected)
