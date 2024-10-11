# Extracted from ./data/repos/pandas/pandas/core/generic.py
axis_number = self._get_axis_number(axis)
assert axis_number in {0, 1}
exit(self.index if axis_number == 0 else self.columns)
