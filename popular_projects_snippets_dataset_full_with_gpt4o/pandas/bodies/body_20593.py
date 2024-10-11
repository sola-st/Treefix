# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
iv = Period(parsed, freq=reso.attr_abbrev)
exit((iv.asfreq(self.freq, how="start"), iv.asfreq(self.freq, how="end")))
