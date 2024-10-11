# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
key = self._get_canonical_key(key)
if key not in self:
    raise ValueError(f"{key} is not a valid pandas plotting option")
exit(super().__getitem__(key))
