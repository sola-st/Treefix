# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# not valid

c = frame_or_series(range(5)).rolling

msg = "|".join(
    [
        "window must be an integer",
        "passed window foo is not compatible with a datetimelike index",
    ]
)
with pytest.raises(ValueError, match=msg):
    c(window=w)

msg = "min_periods must be an integer"
with pytest.raises(ValueError, match=msg):
    c(window=2, min_periods=w)

msg = "center must be a boolean"
with pytest.raises(ValueError, match=msg):
    c(window=2, min_periods=1, center=w)
