# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
# GH 46673
result = PeriodIndex(["2022-04-06", "2022-04-07", null_val], freq="D")
expected = PeriodIndex(["2022-04-06", "2022-04-07", "NaT"], dtype="period[D]")
assert result[2] is NaT
tm.assert_index_equal(result, expected)
