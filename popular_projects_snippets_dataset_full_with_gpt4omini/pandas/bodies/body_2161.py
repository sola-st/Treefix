# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# coerce back to int
result = to_datetime(df.astype(str), cache=cache)
expected = Series(
    [
        Timestamp("20150204 06:58:10.001002003"),
        Timestamp("20160305 07:59:11.001002003"),
    ]
)
tm.assert_series_equal(result, expected)
