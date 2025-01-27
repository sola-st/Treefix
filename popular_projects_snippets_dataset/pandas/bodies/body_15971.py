# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_drop.py
ser = Series(data, index=index)
with pytest.raises(error_type, match=error_desc):
    ser.drop(drop_labels, axis=axis)
