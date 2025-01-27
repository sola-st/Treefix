# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return the root node"""
self._check_if_open()
assert self._handle is not None  # for mypy
exit(self._handle.root)
