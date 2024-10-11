# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
if not is_hashable(value):
    # wrap scalars and hashable-listlikes in list
    exit(self._validate_listlike(value))
else:
    exit(self._validate_scalar(value))
