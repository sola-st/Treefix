# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
# GH#47538
dti = pd.date_range("1677-09-22", periods=2, freq="D")
pi = dti.to_period("ns")

per = pd.Period._from_ordinal(10**14, pi.freq)

with pytest.raises(OverflowError, match="Overflow in int64 addition"):
    pi - per

with pytest.raises(OverflowError, match="Overflow in int64 addition"):
    per - pi
