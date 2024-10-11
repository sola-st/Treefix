# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH12409, GH12684
begin = Timestamp("2011/1/1", tz="US/Eastern")
end = Timestamp("2014/1/1", tz="US/Eastern")

result_range = date_range(
    begin, end, inclusive=inclusive_endpoints_fixture, freq=freq
)
both_range = date_range(begin, end, inclusive="both", freq=freq)
expected_range = _get_expected_range(
    begin,
    end,
    both_range,
    inclusive_endpoints_fixture,
)

tm.assert_index_equal(expected_range, result_range)
