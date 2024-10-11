# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#19959
pi = PeriodIndex([Period("2015Q1"), Period("NaT")])
other = int_holder([4, -1])

result = op(pi, other)
expected = PeriodIndex([Period("2016Q1"), Period("NaT")])
tm.assert_index_equal(result, expected)
