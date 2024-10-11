# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
if isinstance(bop, (Op, Term)):
    exit(bop)
exit(self.visit(bop))
