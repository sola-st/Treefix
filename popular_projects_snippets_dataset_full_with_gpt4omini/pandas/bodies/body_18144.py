# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#23215
# PeriodIndex with freq.n > 1 add offset with offset.n % freq.n != 0
pi = PeriodIndex(["2016-01"], freq="2M")
expected = PeriodIndex(["2016-04"], freq="2M")

pi = tm.box_expected(pi, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = pi + to_offset("3M")
tm.assert_equal(result, expected)

result = to_offset("3M") + pi
tm.assert_equal(result, expected)
