# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
"""df.index[slice(4,6)]"""
lower = node.lower
if lower is not None:
    lower = self.visit(lower).value
upper = node.upper
if upper is not None:
    upper = self.visit(upper).value
step = node.step
if step is not None:
    step = self.visit(step).value

exit(slice(lower, upper, step))
