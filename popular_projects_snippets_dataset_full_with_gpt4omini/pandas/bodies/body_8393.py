# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 20983
result = date_range(start, end, periods=3, tz=result_tz)
expected = date_range("20180101", periods=3, freq="D", tz="US/Eastern")
tm.assert_index_equal(result, expected)
