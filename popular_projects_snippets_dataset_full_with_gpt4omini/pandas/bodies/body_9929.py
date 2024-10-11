# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# not valid

c = frame_or_series(range(5)).expanding
msg = "min_periods must be an integer"
with pytest.raises(ValueError, match=msg):
    c(min_periods=w)
