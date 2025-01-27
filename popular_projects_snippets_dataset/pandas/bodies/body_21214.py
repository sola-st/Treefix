# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
if not isinstance(value, self._scalar_type) and value is not NaT:
    raise ValueError("'value' should be a Timedelta.")
self._check_compatible_with(value)
if value is NaT:
    exit(np.timedelta64(value.value, "ns"))
else:
    exit(value.as_unit(self.unit).asm8)
