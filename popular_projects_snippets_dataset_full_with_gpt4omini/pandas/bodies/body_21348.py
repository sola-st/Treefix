# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
if axis is None or self.ndim == 1:
    exit(self._box_func(result))
exit(self._from_backing_data(result))
