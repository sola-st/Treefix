# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""validate this column: return the compared against itemsize"""
# validate this column for string truncation (or reset to the max size)
if _ensure_decoded(self.kind) == "string":
    c = self.col
    if c is not None:
        if itemsize is None:
            itemsize = self.itemsize
        if c.itemsize < itemsize:
            raise ValueError(
                f"Trying to store a string with len [{itemsize}] in "
                f"[{self.cname}] column but\nthis column has a limit of "
                f"[{c.itemsize}]!\nConsider using min_itemsize to "
                "preset the sizes on these columns"
            )
        exit(c.itemsize)

exit(None)
