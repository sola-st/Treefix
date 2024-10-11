# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "'construct_from_string' expects a string, got <class 'list'>"
with pytest.raises(TypeError, match=msg):
    DatetimeTZDtype.construct_from_string(["datetime64[ns, notatz]"])
