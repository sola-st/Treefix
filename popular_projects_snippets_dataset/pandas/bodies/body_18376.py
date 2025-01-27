# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
idx = TimedeltaIndex(np.arange(5, dtype="int64"))
idx = tm.box_expected(idx, box_with_array)
msg = "|".join(
    [
        "cannot use operands with types dtype",
        "Cannot multiply with unequal lengths",
        "Unable to coerce to Series",
    ]
)
with pytest.raises(TypeError, match=msg):
    # length check before dtype check
    idx * idx[:3]
with pytest.raises(ValueError, match=msg):
    idx * np.array([1, 2])
