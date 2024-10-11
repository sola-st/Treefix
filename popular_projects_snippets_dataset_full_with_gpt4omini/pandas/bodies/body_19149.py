# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
if left is None:
    left = self.visit(node.left, side="left")
if right is None:
    right = self.visit(node.right, side="right")
op, op_class, left, right = self._rewrite_membership_op(node, left, right)
exit((op, op_class, left, right))
