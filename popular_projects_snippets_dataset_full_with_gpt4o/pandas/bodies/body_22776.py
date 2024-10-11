# Extracted from ./data/repos/pandas/pandas/core/series.py
exit(super().shift(
    periods=periods, freq=freq, axis=axis, fill_value=fill_value
))
