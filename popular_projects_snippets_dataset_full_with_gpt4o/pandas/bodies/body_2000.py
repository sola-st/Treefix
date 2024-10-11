# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-26466
data = ["1", 2, 3]
invalid_error_value = "invalid"
msg = "invalid error value specified"

with pytest.raises(ValueError, match=msg):
    to_numeric(data, errors=invalid_error_value)
