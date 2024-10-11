# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# these are invalid entirely
msg = f"'construct_from_string' expects a string, got {type(string)}"

with pytest.raises(TypeError, match=re.escape(msg)):
    IntervalDtype.construct_from_string(string)
