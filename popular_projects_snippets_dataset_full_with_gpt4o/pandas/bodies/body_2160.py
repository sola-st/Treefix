# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
d = {
    "year": "year",
    "month": "month",
    "day": "day",
    "hour": "hour",
    "minute": "minute",
    "second": "second",
    "ms": "ms",
    "us": "us",
    "ns": "ns",
}

result = to_datetime(df.rename(columns=d), cache=cache)
expected = Series(
    [
        Timestamp("20150204 06:58:10.001002003"),
        Timestamp("20160305 07:59:11.001002003"),
    ]
)
tm.assert_series_equal(result, expected)
