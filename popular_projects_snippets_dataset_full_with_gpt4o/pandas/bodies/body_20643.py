# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
if freq is not None and freq != self.freq:
    if isinstance(freq, str):
        freq = to_offset(freq)
    offset = periods * freq
    exit(self + offset)

if periods == 0 or len(self) == 0:
    # GH#14811 empty case
    exit(self.copy())

if self.freq is None:
    raise NullFrequencyError("Cannot shift with no freq")

start = self[0] + periods * self.freq
end = self[-1] + periods * self.freq

# Note: in the DatetimeTZ case, _generate_range will infer the
#  appropriate timezone from `start` and `end`, so tz does not need
#  to be passed explicitly.
result = self._data._generate_range(
    start=start, end=end, periods=None, freq=self.freq
)
exit(type(self)._simple_new(result, name=self.name))
