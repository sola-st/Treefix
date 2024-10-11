# Extracted from ./data/repos/pandas/pandas/tests/extension/test_datetime.py
# Datetime + Datetime not implemented
ser = pd.Series(data)
msg = "cannot add DatetimeArray and DatetimeArray"
with pytest.raises(TypeError, match=msg):
    ser + data
