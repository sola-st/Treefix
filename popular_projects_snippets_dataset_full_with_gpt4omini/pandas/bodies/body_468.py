# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "DatetimeTZDtype only supports s, ms, us, ns units"
with pytest.raises(ValueError, match=msg):
    DatetimeTZDtype("D", "US/Eastern")
