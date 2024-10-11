# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
if not isinstance(value, self._scalar_type) and value is not NaT:
    raise ValueError("'value' should be a Timestamp.")
self._check_compatible_with(value)
if value is NaT:
    exit(np.datetime64(value.value, self.unit))
else:
    exit(value.as_unit(self.unit).asm8)
