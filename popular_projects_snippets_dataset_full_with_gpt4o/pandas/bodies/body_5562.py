# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# Test for #30543
expected = Timestamp("2017-01-01T12")
result = Timestamp(expected)
assert result is expected
