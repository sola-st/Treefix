# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_rendering.py
# pre-1900
stamp = Timestamp("1850-01-01", tz="US/Eastern")
repr(stamp)

iso8601 = "1850-01-01 01:23:45.012345"
stamp = Timestamp(iso8601, tz="US/Eastern")
result = repr(stamp)
assert iso8601 in result
