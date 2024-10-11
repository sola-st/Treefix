# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
key = self._get_canonical_key(key)
if key in self._DEFAULT_KEYS:
    raise ValueError(f"Cannot remove default parameter {key}")
super().__delitem__(key)
