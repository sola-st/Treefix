# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""set the position of this column in the Table"""
self.pos = pos
if pos is not None and self.typ is not None:
    self.typ._v_pos = pos
