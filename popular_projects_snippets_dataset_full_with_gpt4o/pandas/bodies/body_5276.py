# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
per = Period("1990-01-05", "B")  # Friday
result = per.to_timestamp("B", how="E")

expected = Timestamp("1990-01-06") - Timedelta(nanoseconds=1)
assert result == expected
