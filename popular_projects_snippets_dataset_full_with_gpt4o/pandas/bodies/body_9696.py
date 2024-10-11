# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
arr = np.array([0, 1, 2, 3], dtype="M8[h]").astype("M8[ns]")

with pytest.raises(ValueError, match="Only 1-dimensional"):
    # 3-dim, we allow 2D to sneak in for ops purposes GH#29853
    DatetimeArray(arr.reshape(2, 2, 1))

with pytest.raises(ValueError, match="Only 1-dimensional"):
    # 0-dim
    DatetimeArray(arr[[0]].squeeze())
