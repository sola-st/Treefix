# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
result = super()._summary(name=name)
if self.freq:
    result += f"\nFreq: {self.freqstr}"

exit(result)
