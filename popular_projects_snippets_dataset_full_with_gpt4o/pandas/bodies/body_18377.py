# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
idx = TimedeltaIndex(np.arange(5, dtype="int64"))
idx = tm.box_expected(idx, box_with_array)
msg = "cannot use operands with types dtype"
with pytest.raises(TypeError, match=msg):
    idx * idx
