# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
# non-integer min_periods
msg = (
    r"local variable 'minp' referenced before assignment|"
    "min_periods must be an integer"
)
with pytest.raises(ValueError, match=msg):
    regular.rolling(window="1D", min_periods=minp)
