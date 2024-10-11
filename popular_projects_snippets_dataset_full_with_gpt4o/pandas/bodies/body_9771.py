# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 13383
c = frame_or_series(range(5)).rolling

msg = "window must be an integer 0 or greater"

with pytest.raises(ValueError, match=msg):
    c(-1, win_type="boxcar")
