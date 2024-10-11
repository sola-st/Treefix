# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_constructors.py
arr = period_array(["2000", "2001"], freq="D")
with pytest.raises(IncompatibleFrequency, match="freq"):
    PeriodArray(arr, freq="M")

with pytest.raises(IncompatibleFrequency, match="freq"):
    PeriodArray(arr, freq=pd.tseries.offsets.MonthEnd())
