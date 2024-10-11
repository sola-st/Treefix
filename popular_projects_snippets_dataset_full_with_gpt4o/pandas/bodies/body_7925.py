# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# GH#6716
# Confirm DatetimeIndex and PeriodIndex works identically
# getitem against index should raise ValueError
idx = idx_range(start="2013/01/01", freq="D", periods=400)
values = [
    "2014",
    "2013/02",
    "2013/01/02",
    "2013/02/01 9H",
    "2013/02/01 09:00",
]
for val in values:

    # GH7116
    # these show deprecations as we are trying
    # to slice with non-integer indexers
    with pytest.raises(IndexError, match="only integers, slices"):
        idx[val]

ser = Series(np.random.rand(len(idx)), index=idx)
tm.assert_series_equal(ser["2013/01"], ser[0:31])
tm.assert_series_equal(ser["2013/02"], ser[31:59])
tm.assert_series_equal(ser["2014"], ser[365:])

invalid = ["2013/02/01 9H", "2013/02/01 09:00"]
for val in invalid:
    with pytest.raises(KeyError, match=val):
        ser[val]
