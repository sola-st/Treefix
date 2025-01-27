# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# Test for #25057
# Check that we adjust value for fold correctly
# based on timestamps since utc
ts = Timestamp(ts_input, tz=tz, fold=fold)
result = ts.value
expected = value_out
assert result == expected
