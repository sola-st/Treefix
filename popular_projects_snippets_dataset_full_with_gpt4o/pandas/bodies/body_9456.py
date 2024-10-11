# Extracted from ./data/repos/pandas/pandas/tests/arrays/timedeltas/test_constructors.py
# GH#25282
arr = np.array([0, 1, 2, 3], dtype="m8[h]").astype("m8[ns]")

with pytest.raises(ValueError, match="Only 1-dimensional"):
    # 3-dim, we allow 2D to sneak in for ops purposes GH#29853
    TimedeltaArray(arr.reshape(2, 2, 1))

with pytest.raises(ValueError, match="Only 1-dimensional"):
    # 0-dim
    TimedeltaArray(arr[[0]].squeeze())
