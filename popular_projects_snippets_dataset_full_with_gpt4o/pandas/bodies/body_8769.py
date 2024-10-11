# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = PeriodArray(np.arange(3), freq="D")
with pytest.raises(TypeError, match="int"):
    arr[0] = 1
