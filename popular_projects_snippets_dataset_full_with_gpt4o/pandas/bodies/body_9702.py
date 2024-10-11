# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
arr = np.array([1, 2, 3], dtype="bool")

msg = "Unexpected value for 'dtype': 'bool'. Must be"
with pytest.raises(ValueError, match=msg):
    DatetimeArray(arr)

msg = r"dtype bool cannot be converted to datetime64\[ns\]"
with pytest.raises(TypeError, match=msg):
    DatetimeArray._from_sequence(arr)

with pytest.raises(TypeError, match=msg):
    _sequence_to_dt64ns(arr)

with pytest.raises(TypeError, match=msg):
    pd.DatetimeIndex(arr)

with pytest.raises(TypeError, match=msg):
    pd.to_datetime(arr)
