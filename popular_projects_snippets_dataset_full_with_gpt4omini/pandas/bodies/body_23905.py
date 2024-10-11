# Extracted from ./data/repos/pandas/pandas/io/pytables.py
if isinstance(index, MultiIndex):
    setattr(self.attrs, f"{key}_variety", "multi")
    self.write_multi_index(key, index)
else:
    setattr(self.attrs, f"{key}_variety", "regular")
    converted = _convert_index("index", index, self.encoding, self.errors)

    self.write_array(key, converted.values)

    node = getattr(self.group, key)
    node._v_attrs.kind = converted.kind
    node._v_attrs.name = index.name

    if isinstance(index, (DatetimeIndex, PeriodIndex)):
        node._v_attrs.index_class = self._class_to_alias(type(index))

    if isinstance(index, (DatetimeIndex, PeriodIndex, TimedeltaIndex)):
        node._v_attrs.freq = index.freq

    if isinstance(index, DatetimeIndex) and index.tz is not None:
        node._v_attrs.tz = _get_tz(index.tz)
