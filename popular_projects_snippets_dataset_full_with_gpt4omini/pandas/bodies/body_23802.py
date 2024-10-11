# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return the node with the key or None if it does not exist"""
self._check_if_open()
if not key.startswith("/"):
    key = "/" + key

assert self._handle is not None
assert _table_mod is not None  # for mypy
try:
    node = self._handle.get_node(self.root, key)
except _table_mod.exceptions.NoSuchNodeError:
    exit(None)

assert isinstance(node, _table_mod.Node), type(node)
exit(node)
