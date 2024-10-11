# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
# NB: we cannot use self.i8values here because we may have converted
#  the tz in __init__
exit(unique_deltas(self.index.asi8))
