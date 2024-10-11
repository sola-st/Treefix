# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#11497

idx = date_range("2011-01-01", "2011-01-02", freq="D", name="idx")
if to_period:
    idx = idx.to_period("D")
ser = Series([0.1, 0.2], index=idx, name="s")

keys = [Timestamp("2011-01-01"), Timestamp("2011-01-02")]
if to_period:
    keys = [x.to_period("D") for x in keys]
result = ser.loc[keys]
exp = Series([0.1, 0.2], index=idx, name="s")
if not to_period:
    exp.index = exp.index._with_freq(None)
tm.assert_series_equal(result, exp, check_index_type=True)

keys = [
    Timestamp("2011-01-02"),
    Timestamp("2011-01-02"),
    Timestamp("2011-01-01"),
]
if to_period:
    keys = [x.to_period("D") for x in keys]
exp = Series(
    [0.2, 0.2, 0.1], index=Index(keys, name="idx", dtype=idx.dtype), name="s"
)
result = ser.loc[keys]
tm.assert_series_equal(result, exp, check_index_type=True)

keys = [
    Timestamp("2011-01-03"),
    Timestamp("2011-01-02"),
    Timestamp("2011-01-03"),
]
if to_period:
    keys = [x.to_period("D") for x in keys]

with pytest.raises(KeyError, match="not in index"):
    ser.loc[keys]
