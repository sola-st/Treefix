# Extracted from ./data/repos/pandas/pandas/io/pytables.py
if isinstance(alias, type):  # pragma: no cover
    # compat: for a short period of time master stored types
    exit(alias)
exit(self._reverse_index_map.get(alias, Index))
