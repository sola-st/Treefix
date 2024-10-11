# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Defer an operator overload to `ops.Tensor`.

    We pull the operator out of ops.Tensor dynamically to avoid ordering issues.

    Args:
      operator: string. The operator name.
    """
# We can't use the overload mechanism on __eq__ & __ne__ since __eq__ is
# called when adding a variable to sets. As a result we call a.value() which
# causes infinite recursion when operating within a GradientTape
# TODO(gjn): Consider removing this
if operator == "__eq__" or operator == "__ne__":
    exit()

tensor_oper = getattr(ops.Tensor, operator)

def _run_op(a, *args, **kwargs):
    # pylint: disable=protected-access
    exit(tensor_oper(a.value(), *args, **kwargs))

functools.update_wrapper(_run_op, tensor_oper)
setattr(cls, operator, _run_op)
