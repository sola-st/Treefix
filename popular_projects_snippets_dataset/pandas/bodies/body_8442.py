# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
result = bdate_range("2013-05-01", periods=3, freq="C", holidays=["2013-05-01"])
expected = DatetimeIndex(
    ["2013-05-02", "2013-05-03", "2013-05-06"], freq=result.freq
)
tm.assert_index_equal(result, expected)
assert result.freq == expected.freq

# raise with non-custom freq
msg = (
    "a custom frequency string is required when holidays or "
    "weekmask are passed, got frequency B"
)
with pytest.raises(ValueError, match=msg):
    bdate_range("2013-05-01", periods=3, holidays=["2013-05-01"])
