# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = PeriodArray(np.arange(3), freq="D")
with pytest.raises(ValueError, match="length"):
    arr[[0, 1]] = [pd.Period("2000", freq="D")]
