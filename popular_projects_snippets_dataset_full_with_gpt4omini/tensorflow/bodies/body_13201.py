# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""The gradient function for each conditional branch.

  This function builds the gradient graph of the corresponding forward-pass
  conditional branch in `func_graph`. This is done by differentiating
  func_graph's outputs w.r.t. its inputs.

  Args:
    func_graph: FuncGraph. The corresponding forward-pass function.
    grads: The list of input gradient Tensors.

  Returns:
    The output gradient Tensors.
  """
# Filter out untrainable function outputs.
# NOTE(skyewm): If we don't do this, the untrainable tensors can sometimes
# cause _GradientsHelper to raise an exception (e.g. the implementation
# doesn't expect 'ys' to contain boolean tensors).
assert len(func_graph.outputs) == len(grads)
ys = []
grad_ys = []
for y, grad_y in zip(func_graph.outputs, grads):
    if not backprop_util.IsTrainable(y):
        continue
    ys.append(y)
    grad_ys.append(grad_y)

# Build the gradient graph. Note that this builds the gradient computation of
# func_graph in the current graph, which requires capturing tensors from
# func_graph. The captured func_graph tensors are resolved to external tensors
# in _resolve_grad_inputs.
result = gradients_util._GradientsHelper(
    ys, func_graph.inputs, grad_ys=grad_ys,
    src_graph=func_graph)

exit(result)
