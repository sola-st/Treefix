# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
# All cases have (other.month % 3) == (month % 3).
expected = exp_dict.get(n, {}).get(day_opt, n)
assert roll_qtrday(other, n, month, day_opt, modby=3) == expected
