# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
begin = Timestamp("2011/1/1")
end = Timestamp("2014/1/1")
begintz = Timestamp("2011/1/1", tz="US/Eastern")
endtz = Timestamp("2014/1/1", tz="US/Eastern")

result_range = date_range(
    begin,
    end,
    inclusive=inclusive_endpoints_fixture,
    freq=freq,
    tz="US/Eastern",
)
both_range = date_range(
    begin, end, inclusive="both", freq=freq, tz="US/Eastern"
)
expected_range = _get_expected_range(
    begintz,
    endtz,
    both_range,
    inclusive_endpoints_fixture,
)

tm.assert_index_equal(expected_range, result_range)
