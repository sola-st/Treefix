# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-19124
vec = box(["1 day", "2 day"], dtype="timedelta64[ns]")
box_nat = box([NaT, NaT], dtype="timedelta64[ns]")
tm.assert_equal(_ops[op_name](vec, NaT), box_nat)
