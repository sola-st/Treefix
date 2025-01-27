# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 24329
# Make sure that calling Timestamp constructor
# on Timestamp created from ambiguous time
# doesn't change Timestamp.value
ts = Timestamp(1382835600000000000, tz="dateutil/Europe/London")
expected = ts.value
result = Timestamp(ts).value
assert result == expected
