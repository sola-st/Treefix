# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
start = Timestamp("2022-10-19 11:50:44.719781")
end = Timestamp("2022-10-19 11:50:47.066458")

# start and end cannot be cast to "s" unit without lossy rounding,
#  so we do not allow this in date_range
with pytest.raises(ValueError, match="Cannot losslessly convert units"):
    date_range(start, end, periods=3, unit="s")

# but we can losslessly cast to "us"
dti = date_range(start, end, periods=2, unit="us")
rng = np.array(
    [start.as_unit("us").value, end.as_unit("us").value], dtype=np.int64
)
expected = DatetimeIndex(rng.view("M8[us]"))
tm.assert_index_equal(dti, expected)
