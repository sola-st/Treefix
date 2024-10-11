# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_insert.py
# GH#18295 (test missing)
expected = PeriodIndex(["2017Q1", NaT, "2017Q2", "2017Q3", "2017Q4"], freq="Q")
result = period_range("2017Q1", periods=4, freq="Q").insert(1, na)
tm.assert_index_equal(result, expected)
