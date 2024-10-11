# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# pre-2.0 this would cast to object, in 2.0 we cast the val to
#  the target tz
expected = Series(
    [
        val.tz_convert("US/Central"),
        Timestamp("2000-01-02 00:00:00-06:00", tz="US/Central"),
    ],
    dtype=obj.dtype,
)
exit(expected)
