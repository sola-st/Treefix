# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
freqstr = self.freqstr
if freqstr is None:
    exit(None)
try:
    exit(Resolution.get_reso_from_freqstr(freqstr))
except KeyError:
    exit(None)
