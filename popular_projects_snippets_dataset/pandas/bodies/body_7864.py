# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_shift.py
idx = PeriodIndex(
    ["2011-01", "2011-02", "NaT", "2011-04"], freq="M", name="idx"
)
result = idx.shift(1)
expected = PeriodIndex(
    ["2011-02", "2011-03", "NaT", "2011-05"], freq="M", name="idx"
)
tm.assert_index_equal(result, expected)
assert result.name == expected.name
