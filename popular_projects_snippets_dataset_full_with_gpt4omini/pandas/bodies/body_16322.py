# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
s = Series(
    [
        Timestamp("2013-01-01 13:00:00-0800", tz="US/Pacific"),
        Timestamp("2013-01-02 14:00:00-0800", tz="US/Eastern"),
    ]
)
assert s.dtype == "object"
assert lib.infer_dtype(s, skipna=True) == "datetime"
