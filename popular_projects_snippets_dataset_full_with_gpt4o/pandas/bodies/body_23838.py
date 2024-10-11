# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""set my state from the passed info"""
idx = info.get(self.name)
if idx is not None:
    self.__dict__.update(idx)
