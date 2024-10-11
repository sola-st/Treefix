# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
"""create and return the op string for this TermValue"""
val = v.tostring(self.encoding)
exit(f"({self.lhs} {self.op} {val})")
