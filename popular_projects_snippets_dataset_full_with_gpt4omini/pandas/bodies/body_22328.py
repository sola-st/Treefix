# Extracted from ./data/repos/pandas/pandas/core/resample.py
if self.kind == "timestamp":
    exit(super()._get_binner_for_time())
exit(self.groupby._get_period_bins(self.ax))
