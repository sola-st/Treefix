# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
axis = self._normalize_axis(axis)
if fill_value is lib.no_default:
    fill_value = None

exit(self.apply("shift", periods=periods, axis=axis, fill_value=fill_value))
