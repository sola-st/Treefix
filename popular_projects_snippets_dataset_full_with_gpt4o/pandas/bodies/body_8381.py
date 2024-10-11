# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# cases where stride * periods overflow int64 and stride/endpoint
#  have different signs
start = Timestamp("2262-02-23")
end = Timestamp("1969-11-14")

expected = date_range(start=start, end=end, freq="-1H")
assert expected[0] == start
assert expected[-1] == end

dti = date_range(end=end, periods=len(expected), freq="-1H")
tm.assert_index_equal(dti, expected)

start2 = Timestamp("1970-02-01")
end2 = Timestamp("1677-10-22")

expected2 = date_range(start=start2, end=end2, freq="-1H")
assert expected2[0] == start2
assert expected2[-1] == end2

dti2 = date_range(start=start2, periods=len(expected2), freq="-1H")
tm.assert_index_equal(dti2, expected2)
