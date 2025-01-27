# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
"""Return new `LinearOperator` acting like `op1 + op2`.

    Args:
      op1:  `LinearOperator`
      op2:  `LinearOperator`, with `shape` and `dtype` such that adding to
        `op1` is allowed.
      operator_name:  `String` name to give to returned `LinearOperator`
      hints:  `_Hints` object.  Returned `LinearOperator` will be created with
        these hints.

    Returns:
      `LinearOperator`
    """
updated_hints = _infer_hints_allowing_override(op1, op2, hints)

if operator_name is None:
    operator_name = "Add/" + op1.name + "__" + op2.name + "/"

scope_name = self.name
if scope_name.startswith("_"):
    scope_name = scope_name[1:]
with ops.name_scope(scope_name):
    exit(self._add(op1, op2, operator_name, updated_hints))
