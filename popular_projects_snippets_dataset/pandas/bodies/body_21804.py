# Extracted from ./data/repos/pandas/pandas/core/window/online.py
result, old_wt = ewm_func(
    weighted_avg,
    deltas,
    min_periods,
    self.old_wt_factor,
    self.new_wt,
    self.old_wt,
    self.adjust,
    self.ignore_na,
)
self.old_wt = old_wt
self.last_ewm = result[-1]
exit(result)
