# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        maybe set a string col itemsize:
            min_itemsize can be an integer or a dict with this columns name
            with an integer size
        """
if _ensure_decoded(self.kind) == "string":
    if isinstance(min_itemsize, dict):
        min_itemsize = min_itemsize.get(self.name)

    if min_itemsize is not None and self.typ.itemsize < min_itemsize:
        self.typ = _tables().StringCol(itemsize=min_itemsize, pos=self.pos)
