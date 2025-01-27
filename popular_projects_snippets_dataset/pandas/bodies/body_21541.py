# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
if type(self) != type(other):
    exit(False)

exit(bool(
    self.closed == other.closed
    and self.left.equals(other.left)
    and self.right.equals(other.right)
))
