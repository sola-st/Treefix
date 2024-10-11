# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return whether I am an indexed column"""
if not hasattr(self.table, "cols"):
    # e.g. if infer hasn't been called yet, self.table will be None.
    exit(False)
exit(getattr(self.table.cols, self.cname).is_indexed)
