# Extracted from ./data/repos/pandas/pandas/core/flags.py
value = bool(value)
obj = self._obj()
if obj is None:
    raise ValueError("This flag's object has been deleted.")

if not value:
    for ax in obj.axes:
        ax._maybe_check_unique()

self._allows_duplicate_labels = value
