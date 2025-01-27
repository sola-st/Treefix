# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Builds and returns the gradient FuncGraph of `func_graph` and its args.

  The returned grad_func_graph must be called with the returned
  args + grad_func_graph.captures.

  Args:
    ys: A `Tensor` or list of tensors to be differentiated.
    xs: A `Tensor` or list of tensors to be used for differentiation.
    grads: The incoming grads for `ys`.
    cond_graph: FuncGraph for the forward cond function.
    body_graph: FuncGraph for the forward body function.
    name: Name of the returned gradient function.
    while_op: The forward While op.
    maximum_iterations: Tensor. The maximum number of iterations.
    stateful_parallelism: Bool, see tf.while_loop.

  Returns:
    2-tuple of (grad_func_graph, args).
  """
assert len(ys) == len(grads)

total_iters = while_op.outputs[0]
counter = constant_op.constant(
    0, dtype=total_iters.dtype, name="grad_counter")

# Build frozen sets so that we do not have linear time lookups in
# `_is_loop_invariant`. Note: `body_graph.inputs` and `body_graph.outputs`
# may get updated during gradient computation because we add accumulators to
# the forward op. However, those are not loop invariants so wouldn't affect
# the output of `_is_loop_invariant`. Also we would never attempt to capture
# those accumulators so `_is_loop_invariant` should never receive those new
# tensors as args.
body_graph_inputs = object_identity.ObjectIdentitySet(body_graph.inputs)
body_graph_outputs = object_identity.ObjectIdentitySet(body_graph.outputs)

args = [counter, maximum_iterations, total_iters] + list(grads)
# Note: The returned function does not have `args` in the list of
# `external_captures`.
grad_func_graph = func_graph_module.func_graph_from_py_func(
    name,
    lambda *args: _grad_fn(ys, xs, args, body_graph),
    args, {},
    func_graph=_WhileBodyGradFuncGraph(name, cond_graph, body_graph,
                                       maximum_iterations, while_op,
                                       body_graph_inputs, body_graph_outputs),
    acd_record_initial_resource_uses=stateful_parallelism)

# Update the list of outputs with tensors corresponding to the captured
# tensors. We capture 3 types of tensors when building the grad fn:
# 1. Accumulators for forward graph intermediates which are not loop
#    invariants. The outputs corresponding to these are populated in
#    `internal_capture_to_output` by `_WhileBodyGradFuncGraph`.
# 2. Resources, which are output as is.
# 3. Forward graph loop invariants, which are output as is.
for external_capture, internal_capture in grad_func_graph.captures:
    if (ops.tensor_id(internal_capture)
        in grad_func_graph.internal_capture_to_output):
        new_output = grad_func_graph.internal_capture_to_output[ops.tensor_id(
            internal_capture)]
    else:
        raise ValueError(
            f"Tensor {str(internal_capture)} which captures "
            f"{str(external_capture)} is in list of "
            f"internal_captures but not in internal_capture_to_output.")
    grad_func_graph.outputs.append(new_output)
    grad_func_graph.structured_outputs.append(new_output)

exit((grad_func_graph, args))
