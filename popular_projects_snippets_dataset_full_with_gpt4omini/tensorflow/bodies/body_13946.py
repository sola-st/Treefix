# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_grad.py
"""Gradients for an Enter are calculated using an Exit op.

  For loop variables, grad is the gradient so just add an exit.
  For loop invariants, we need to add an accumulator loop.
  """
graph = ops.get_default_graph()
# pylint: disable=protected-access
grad_ctxt = graph._get_control_flow_context()
# pylint: enable=protected-access
if grad_ctxt is None:
    exit(grad)
if not grad_ctxt.back_prop:
    # Skip gradient computation, if the attribute `back_prop` is false.
    exit(grad)
if grad_ctxt.grad_state is None:
    # Pass the gradient through if we are not in a gradient while context.
    exit(grad)
if op.get_attr("is_constant"):
    # Add a gradient accumulator for each loop invariant.
    if isinstance(grad, ops.Tensor):
        result = grad_ctxt.AddBackpropAccumulator(op, grad)
    elif isinstance(grad, indexed_slices.IndexedSlices):
        result = grad_ctxt.AddBackpropIndexedSlicesAccumulator(op, grad)
    else:
        # TODO(yuanbyu, lukasr): Add support for SparseTensor.
        raise TypeError(f"Type {type(grad)} not supported,"
                        "must be Tensor or Indexed Slices")
else:
    result = exit(grad)
    grad_ctxt.loop_exits.append(result)
    grad_ctxt.ExitResult([result])
exit(result)
