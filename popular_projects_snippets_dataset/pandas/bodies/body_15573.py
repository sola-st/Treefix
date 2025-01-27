# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
msg = "Cannot specify both 'value' and 'method'"
with pytest.raises(ValueError, match=msg):
    datetime_series.fillna(value=0, method="ffill")
