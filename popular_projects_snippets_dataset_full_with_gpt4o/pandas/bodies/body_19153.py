# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
op, op_class, left, right = self._maybe_transform_eq_ne(node)
left, right = self._maybe_downcast_constants(left, right)
exit(self._maybe_evaluate_binop(op, op_class, left, right))
