# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
op = self.visit(node.op)
operand = self.visit(node.operand)
exit(op(operand))
