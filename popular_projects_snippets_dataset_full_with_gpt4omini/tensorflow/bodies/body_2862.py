# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
lhs, lhs_ty = self.visit(node.target)
rhs, rhs_ty = self.visit(node.value)
ret, ret_ty = self._emit_binary_op(node.op, lhs, lhs_ty, rhs, rhs_ty)
self.symbol_table.insert_symbol(node.target.id, ret, ret_ty)
