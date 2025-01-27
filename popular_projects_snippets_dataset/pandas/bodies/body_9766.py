# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# not valid

c = frame_or_series(range(5)).rolling
with pytest.raises(ValueError, match="min_periods must be an integer"):
    c(win_type="boxcar", window=2, min_periods=w)
with pytest.raises(ValueError, match="center must be a boolean"):
    c(win_type="boxcar", window=2, min_periods=1, center=w)
