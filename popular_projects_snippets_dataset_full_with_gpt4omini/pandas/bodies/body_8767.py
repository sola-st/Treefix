# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = PeriodArray(np.arange(3), freq="D")
with pytest.raises(IncompatibleFrequency, match="freq"):
    arr[0] = pd.Period("2000", freq="A")

other = period_array(["2000", "2001"], freq="A")
with pytest.raises(IncompatibleFrequency, match="freq"):
    arr[[0, 1]] = other
