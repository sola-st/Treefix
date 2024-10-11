# Extracted from ./data/repos/pandas/pandas/io/pytables.py
assert isinstance(parent, HDFStore), type(parent)
assert _table_mod is not None  # needed for mypy
assert isinstance(group, _table_mod.Node), type(group)
self.parent = parent
self.group = group
self.encoding = _ensure_encoding(encoding)
self.errors = errors
