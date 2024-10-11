# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# GH#6716
didx = date_range(start="2013/01/01 09:00:00", freq="S", periods=4000)
pidx = period_range(start="2013/01/01 09:00:00", freq="S", periods=4000)

for idx in [didx, pidx]:
    # getitem against index should raise ValueError
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
    tm.assert_series_equal(ser["2013/01/01 10:00"], ser[3600:3660])
    tm.assert_series_equal(ser["2013/01/01 9H"], ser[:3600])
    for d in ["2013/01/01", "2013/01", "2013"]:
        tm.assert_series_equal(ser[d], ser)
