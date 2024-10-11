# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
with pytest.raises(ValueError, match="Frequency inference"):
    DatetimeArray(np.array([1, 2, 3], dtype="i8"), freq="infer")
