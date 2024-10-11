# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
try:
    period = Period(label, freq=self.freq)
except ValueError as err:
    # we cannot construct the Period
    raise KeyError(label) from err
exit(period)
