# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
nmonths = self.fields["Y"] * 12 + self.fields["M"]
exit(unique_deltas(nmonths.astype("i8")))
