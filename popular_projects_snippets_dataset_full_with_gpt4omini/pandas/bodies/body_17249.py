# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
ser = Series([1])
msg = "No axis named 1 for object type Series"
with pytest.raises(ValueError, match=msg):
    ser._set_axis_name(name="a", axis=1)
