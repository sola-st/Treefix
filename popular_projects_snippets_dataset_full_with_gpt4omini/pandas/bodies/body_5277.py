# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH 24444
result = Period(ts).to_timestamp(freq=freq).microsecond
assert result == expected
