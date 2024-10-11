# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Computes the gradient of `func_graph` in the current graph.

  This function builds the gradient graph of the corresponding forward-pass
  `func_graph` by differentiating `func_graph`'s outputs w.r.t. its inputs.

  Args:
    ys: A `Tensor` or list of tensors to be differentiated.
    xs: A `Tensor` or list of tensors to be used for differentiation.
    args: The input arguments.
      args[0] - Loop counter
      args[1] - Total number of iterations.
      args[2] - maximum_iterations.
      args[3:] - Incoming gradients for `ys`.
    func_graph: function.FuncGraph. The corresponding forward-pass function.

  Returns:
    The output gradient Tensors.
  """
grad_ys = args[3:]

# Build the gradient graph. Note that this builds the gradient computation of
# func_graph in the current graph, which requires capturing tensors from
# func_graph. The captured func_graph tensors are resolved to external tensors
# after the forward While op has been rewritten in _resolve_grad_captures.
# TODO(srbs): Mark GradientsHelper as public?
grad_outs = gradients_util._GradientsHelper(
    ys, xs, grad_ys=grad_ys, src_graph=func_graph,
    unconnected_gradients="zero")

# TODO(b/118712257): Handle the case when grad_outs has None's e.g. when there
# is a tf.StopGradient in the loop body.
assert all(g is not None for g in grad_outs)
counter = args[0]
maximum_iterations = args[1]
total_iters = args[2]
exit([counter + 1, maximum_iterations, total_iters] + grad_outs)
