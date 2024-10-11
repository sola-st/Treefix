# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_partial_slicing.py
# GH#6716
idx = make_range(start="2013/01/01 09:00:00", freq="S", periods=4000)
msg = "slice indices must be integers or None or have an __index__ method"

# slices against index should raise IndexError
values = [
    "2014",
    "2013/02",
    "2013/01/02",
    "2013/02/01 9H",
    "2013/02/01 09:00",
]
for v in values:
    with pytest.raises(TypeError, match=msg):
        idx[v:]

s = Series(np.random.rand(len(idx)), index=idx)

tm.assert_series_equal(s["2013/01/01 09:05":"2013/01/01 09:10"], s[300:660])
tm.assert_series_equal(s["2013/01/01 10:00":"2013/01/01 10:05"], s[3600:3960])
tm.assert_series_equal(s["2013/01/01 10H":], s[3600:])
tm.assert_series_equal(s[:"2013/01/01 09:30"], s[:1860])
for d in ["2013/01/01", "2013/01", "2013"]:
    tm.assert_series_equal(s[d:], s)
