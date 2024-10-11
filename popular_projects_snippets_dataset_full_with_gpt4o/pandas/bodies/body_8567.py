# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# if we already have a tz and its not the same, then raise
idx = DatetimeIndex(
    ["2013-01-01", "2013-01-02"], dtype="datetime64[ns, US/Eastern]"
)

msg = (
    "cannot supply both a tz and a timezone-naive dtype "
    r"\(i\.e\. datetime64\[ns\]\)"
)
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(idx, dtype="datetime64[ns]")

# this is effectively trying to convert tz's
msg = "data is already tz-aware US/Eastern, unable to set specified tz: CET"
with pytest.raises(TypeError, match=msg):
    DatetimeIndex(idx, dtype="datetime64[ns, CET]")
msg = "cannot supply both a tz and a dtype with a tz"
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(idx, tz="CET", dtype="datetime64[ns, US/Eastern]")

result = DatetimeIndex(idx, dtype="datetime64[ns, US/Eastern]")
tm.assert_index_equal(idx, result)
