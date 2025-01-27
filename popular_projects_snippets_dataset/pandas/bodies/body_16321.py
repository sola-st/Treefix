# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# inference
s = Series(
    [
        Timestamp("2013-01-01 13:00:00-0800", tz="US/Pacific"),
        Timestamp("2013-01-02 14:00:00-0800", tz="US/Pacific"),
    ]
)
assert s.dtype == "datetime64[ns, US/Pacific]"
assert lib.infer_dtype(s, skipna=True) == "datetime64"
