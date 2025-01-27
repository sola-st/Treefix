# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# GH#24391
pi = period_range("2018-01-01", periods=3, freq="2D")
with pytest.raises(AssertionError, match="ndarray"):
    pi._shallow_copy(pi.asi8)
