# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 17415: With naive string
result = Series([arg], dtype="datetime64[ns, CET]")
expected = Series(Timestamp(arg)).dt.tz_localize("CET")
tm.assert_series_equal(result, expected)
