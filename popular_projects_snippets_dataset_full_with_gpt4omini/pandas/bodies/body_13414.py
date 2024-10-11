# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# edge case that converts postgresql datetime with time zone types
# to datetime64[ns,psycopg2.tz.FixedOffsetTimezone..], which is ok
# but should be more natural, so coerce to datetime64[ns] for now

def check(col):
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

        # GH11216
df = read_sql_query("select * from types", self.conn)
if not hasattr(df, "DateColWithTz"):
    request.node.add_marker(
        pytest.mark.xfail(reason="no column with datetime with time zone")
    )

# this is parsed on Travis (linux), but not on macosx for some reason
# even with the same versions of psycopg2 & sqlalchemy, possibly a
# Postgresql server version difference
col = df.DateColWithTz
assert is_datetime64tz_dtype(col.dtype)

df = read_sql_query(
    "select * from types", self.conn, parse_dates=["DateColWithTz"]
)
if not hasattr(df, "DateColWithTz"):
    request.node.add_marker(
        pytest.mark.xfail(reason="no column with datetime with time zone")
    )
col = df.DateColWithTz
assert is_datetime64tz_dtype(col.dtype)
assert str(col.dt.tz) == "UTC"
check(df.DateColWithTz)

df = concat(
    list(read_sql_query("select * from types", self.conn, chunksize=1)),
    ignore_index=True,
)
col = df.DateColWithTz
assert is_datetime64tz_dtype(col.dtype)
assert str(col.dt.tz) == "UTC"
expected = sql.read_sql_table("types", self.conn)
col = expected.DateColWithTz
assert is_datetime64tz_dtype(col.dtype)
tm.assert_series_equal(df.DateColWithTz, expected.DateColWithTz)

# xref #7139
# this might or might not be converted depending on the postgres driver
df = sql.read_sql_table("types", self.conn)
check(df.DateColWithTz)
