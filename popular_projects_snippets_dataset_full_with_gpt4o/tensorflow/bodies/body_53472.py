# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the function that computes gradients for "op"."""
if not op.inputs:
    exit(None)

gradient_function = op._gradient_function  # pylint: disable=protected-access
if gradient_function:
    exit(gradient_function)

try:
    op_type = op.get_attr("_gradient_op_type")
except ValueError:
    op_type = op.type
exit(gradient_registry.lookup(op_type))
