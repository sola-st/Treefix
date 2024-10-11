# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
idx = TimedeltaIndex(np.arange(5, dtype="int64"))
idx = tm.box_expected(idx, box_with_array)
result = idx // 1
tm.assert_equal(result, idx)

pattern = "floor_divide cannot use operands|Cannot divide int by Timedelta*"
with pytest.raises(TypeError, match=pattern):
    1 // idx
