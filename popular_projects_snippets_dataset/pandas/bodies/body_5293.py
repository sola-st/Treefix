# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH#34449
per = Period("1990-01-05", "B")
result = per.end_time

expected = Timestamp("1990-01-06") - Timedelta(nanoseconds=1)
assert result == expected
