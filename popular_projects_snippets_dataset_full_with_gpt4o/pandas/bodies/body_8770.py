# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = period_array(["2000", "2001"], freq="D")
other = pd.Period("2000", freq="M")
with pytest.raises(IncompatibleFrequency, match="freq"):
    arr - other
