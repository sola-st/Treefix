# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
orig = Series(date_range("2016-01-01", freq="H", periods=3, tz=tz))
assert orig.dtype == f"datetime64[ns, {tz}]"

exp = Series(
    [
        Timestamp("2016-01-01 00:00", tz=tz),
        Timestamp("2011-01-01 00:00", tz=tz),
        Timestamp("2016-01-01 02:00", tz=tz),
    ]
)

# scalar
ser = orig.copy()
indexer_sli(ser)[1] = Timestamp("2011-01-01", tz=tz)
tm.assert_series_equal(ser, exp)

# vector
vals = Series(
    [Timestamp("2011-01-01", tz=tz), Timestamp("2012-01-01", tz=tz)],
    index=[1, 2],
)
assert vals.dtype == f"datetime64[ns, {tz}]"

exp = Series(
    [
        Timestamp("2016-01-01 00:00", tz=tz),
        Timestamp("2011-01-01 00:00", tz=tz),
        Timestamp("2012-01-01 00:00", tz=tz),
    ]
)

ser = orig.copy()
indexer_sli(ser)[[1, 2]] = vals
tm.assert_series_equal(ser, exp)
