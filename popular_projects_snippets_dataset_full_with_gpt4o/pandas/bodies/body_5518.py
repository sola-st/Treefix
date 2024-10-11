# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
now = datetime.utcnow()
ts = Timestamp(now).as_unit("ns")
result = ts + other
valdiff = result.value - ts.value
assert valdiff == expected_difference

ts2 = Timestamp(now)
assert ts2 + other == result
