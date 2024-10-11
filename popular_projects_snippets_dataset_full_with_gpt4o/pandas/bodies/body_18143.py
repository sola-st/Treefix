# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#23215
# add offset to PeriodIndex with freq.n > 1

per = Period("2016-01", freq="2M")
pi = PeriodIndex([per])

expected = PeriodIndex(["2016-03"], freq="2M")

pi = tm.box_expected(pi, box_with_array, transpose=transpose)
expected = tm.box_expected(expected, box_with_array, transpose=transpose)

result = pi + per.freq
tm.assert_equal(result, expected)

result = per.freq + pi
tm.assert_equal(result, expected)
