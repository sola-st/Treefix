# Extracted from ./data/repos/pandas/pandas/core/resample.py

# this is how we are actually creating the bins
if self.kind == "period":
    exit(self.groupby._get_time_period_bins(self.ax))
exit(self.groupby._get_time_bins(self.ax))
