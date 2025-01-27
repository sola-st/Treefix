# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# Test for #25057
# Check that we infer fold correctly based on timestamps since utc
# or strings
ts = Timestamp(ts_input, tz=tz)
result = ts.fold
expected = fold_out
assert result == expected
