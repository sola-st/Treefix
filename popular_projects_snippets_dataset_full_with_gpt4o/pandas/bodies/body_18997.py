# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
exit(all(operand.is_scalar for operand in self.operands))
