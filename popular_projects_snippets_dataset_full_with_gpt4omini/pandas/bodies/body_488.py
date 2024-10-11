# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = f"Cannot construct a 'PeriodDtype' from '{string}'"
with pytest.raises(TypeError, match=re.escape(msg)):
    PeriodDtype.construct_from_string(string)
