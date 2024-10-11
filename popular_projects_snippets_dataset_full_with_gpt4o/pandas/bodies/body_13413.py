# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# check that a column is either datetime64[ns]
# or datetime64[ns, UTC]
if is_datetime64_dtype(col.dtype):

    # "2000-01-01 00:00:00-08:00" should convert to
    # "2000-01-01 08:00:00"
    assert col[0] == Timestamp("2000-01-01 08:00:00")

    # "2000-06-01 00:00:00-07:00" should convert to
    # "2000-06-01 07:00:00"
    assert col[1] == Timestamp("2000-06-01 07:00:00")

elif is_datetime64tz_dtype(col.dtype):
    assert str(col.dt.tz) == "UTC"

    # "2000-01-01 00:00:00-08:00" should convert to
    # "2000-01-01 08:00:00"
    # "2000-06-01 00:00:00-07:00" should convert to
    # "2000-06-01 07:00:00"
    # GH 6415
    expected_data = [
        Timestamp("2000-01-01 08:00:00", tz="UTC"),
        Timestamp("2000-06-01 07:00:00", tz="UTC"),
    ]
    expected = Series(expected_data, name=col.name)
    tm.assert_series_equal(col, expected)

else:
    raise AssertionError(
        f"DateCol loaded with incorrect type -> {col.dtype}"
    )
