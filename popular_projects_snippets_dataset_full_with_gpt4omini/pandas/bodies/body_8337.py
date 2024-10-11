# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
dti = date_range("20130101 09:10:11", periods=5)
dti = dti.tz_localize("UTC").tz_convert("US/Eastern")
with pytest.raises(ValueError, match=error_msg):
    dti.round(freq)
