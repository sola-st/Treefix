# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# Test for #30543
expected = Timedelta(np.timedelta64(1, "s"))
result = Timedelta(expected)
assert result is expected
