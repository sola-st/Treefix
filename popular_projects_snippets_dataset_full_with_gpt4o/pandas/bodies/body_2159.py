# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# unit mappings
result = to_datetime(df[list(unit.keys())].rename(columns=unit), cache=cache)
expected = Series(
    [Timestamp("20150204 06:58:10"), Timestamp("20160305 07:59:11")]
)
tm.assert_series_equal(result, expected)
