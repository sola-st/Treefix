# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
exit(window_aggregations.ewmcov(
    X,
    start,
    end,
    min_periods,
    Y,
    self._com,
    self.adjust,
    self.ignore_na,
    True,
))
