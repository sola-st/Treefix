# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
"""create and return a new specialized BinOp from myself"""
if left is None:
    exit(right)
elif right is None:
    exit(left)

k = klass
if isinstance(left, ConditionBinOp):
    if isinstance(right, ConditionBinOp):
        k = JointConditionBinOp
    elif isinstance(left, k):
        exit(left)
    elif isinstance(right, k):
        exit(right)

elif isinstance(left, FilterBinOp):
    if isinstance(right, FilterBinOp):
        k = JointFilterBinOp
    elif isinstance(left, k):
        exit(left)
    elif isinstance(right, k):
        exit(right)

exit(k(
    self.op, left, right, queryables=self.queryables, encoding=self.encoding
).evaluate())
