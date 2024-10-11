# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 12669

c = frame_or_series(range(5)).rolling

# valid
c(0)
c(window=2)
c(window=2, min_periods=1)
c(window=2, min_periods=1, center=True)
c(window=2, min_periods=1, center=False)

# GH 13383

msg = "window must be an integer 0 or greater"

with pytest.raises(ValueError, match=msg):
    c(-1)
