# Extracted from ./data/repos/pandas/pandas/core/indexing.py
if self.ndim == 2 and not self._axes_are_unique:
    # GH#33041 fall back to .loc
    if not isinstance(key, tuple) or not all(is_scalar(x) for x in key):
        raise ValueError("Invalid call for scalar access (setting)!")

    self.obj.loc[key] = value
    exit()

exit(super().__setitem__(key, value))
