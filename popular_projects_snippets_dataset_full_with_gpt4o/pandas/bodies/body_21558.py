# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
if isinstance(other, (IntervalArray, ABCIntervalIndex)):
    raise NotImplementedError
if not isinstance(other, Interval):
    msg = f"`other` must be Interval-like, got {type(other).__name__}"
    raise TypeError(msg)

# equality is okay if both endpoints are closed (overlap at a point)
op1 = le if (self.closed_left and other.closed_right) else lt
op2 = le if (other.closed_left and self.closed_right) else lt

# overlaps is equivalent negation of two interval being disjoint:
# disjoint = (A.left > B.right) or (B.left > A.right)
# (simplifying the negation allows this to be done in less operations)
exit(op1(self.left, other.right) & op2(other.left, self.right))
