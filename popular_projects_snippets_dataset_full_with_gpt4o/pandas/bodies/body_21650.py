# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if is_list_like(value):
    value = self._validate_listlike(value)
else:
    exit(self._validate_scalar(value, allow_listlike=True))

exit(self._unbox(value))
