# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
c = frame_or_series(range(5)).rolling
with pytest.raises(ValueError, match="Invalid win_type"):
    c(win_type=wt, window=2)
