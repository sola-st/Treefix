# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
with pytest.raises(ValueError, match="step must be >= 0"):
    DataFrame(range(2)).rolling(1, step=-1)
