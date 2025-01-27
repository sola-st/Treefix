# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 6673
start = "2018-07-21"  # Saturday
end = "2018-07-29"  # Sunday
result = date_range(start, end, freq="B", inclusive=inclusive)

bday_start = "2018-07-23"  # Monday
bday_end = "2018-07-27"  # Friday
expected = date_range(bday_start, bday_end, freq="D")
tm.assert_index_equal(result, expected)
