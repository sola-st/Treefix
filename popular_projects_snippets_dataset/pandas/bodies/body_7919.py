# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
idx = period_range("2007-01", periods=10, freq="M", name="x")

result = idx[[1, 3, 5]]
exp = PeriodIndex(["2007-02", "2007-04", "2007-06"], freq="M", name="x")
tm.assert_index_equal(result, exp)

result = idx[[True, True, False, False, False, True, True, False, False, False]]
exp = PeriodIndex(
    ["2007-01", "2007-02", "2007-06", "2007-07"], freq="M", name="x"
)
tm.assert_index_equal(result, exp)
