# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = f"Cannot construct a 'DatetimeTZDtype' from '{string}'"
with pytest.raises(TypeError, match=re.escape(msg)):
    DatetimeTZDtype.construct_from_string(string)
