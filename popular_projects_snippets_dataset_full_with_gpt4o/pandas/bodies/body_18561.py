# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
expected = {3: {-3: -2, 4: 4}, 5: {-3: -3, 4: 3}}

other = Timestamp(2072, 10, 1, 6, 17, 18)  # Saturday.
assert roll_qtrday(other, n, month, day_opt, modby=3) == expected[month][n]
