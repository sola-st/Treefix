# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
lhs, lhs_ty = self.visit(node.left)
rhs, rhs_ty = self.visit(node.right)
exit(self._emit_binary_op(node.op, lhs, lhs_ty, rhs, rhs_ty))
