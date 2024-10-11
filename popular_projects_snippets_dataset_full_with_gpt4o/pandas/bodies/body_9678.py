# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_constructors.py
ser = pd.Series([1, 2, 3])
with pytest.raises(TypeError, match="dtype"):
    PeriodArray(ser, freq="D")
