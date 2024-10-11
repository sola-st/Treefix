# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# U was used as undefined period
with pytest.raises(ValueError, match="Invalid frequency: X"):
    period_range("2007-1-1", periods=500, freq="X")
