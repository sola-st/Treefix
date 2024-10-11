# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# Convert our i8 representations to RangeIndex
# Caller is responsible for checking isinstance(self.freq, Tick)
freq = cast(Tick, self.freq)
tick = freq.delta.value
rng = range(self[0].value, self[-1].value + tick, tick)
exit(RangeIndex(rng))
