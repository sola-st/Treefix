# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
"""Rewrites grad_output_slices's corresponding input to be an IndexedSlices.

  This rewrite requires that forward_input was captured in the forward loop,
  i.e. is not a user-specified loop variable. This is important because the
  rewrite assumes that forward_input is passed through to its corresponding
  output unchanged. This assumption is used in _rewrite_input_as_indexed_slices,
  which depends on the exact gradient structure produced by the input's fanout.

  This can yield a more efficient computation than using
  _rewrite_output_as_tensor, since it preserves the IndexedSlices structure
  instead of converting the IndexedSlices to a dense Tensor.

  Args:
    body_grad_graph: _WhileBodyGradFuncGraph.
    grad_output_slices: IndexedSlices output of body_grad_graph.
    forward_input: the corresponding Tensor input to the forward loop.
    loop_vars: list of Tensors. The inputs to body_grad_graph.

  Returns:
    The new loop_vars to pass to body_grad_graph.
  """
# Create initial IndexedSlices that will be the input to the grad While
# op. This will start as zeros, and accumulate the IndexedSlices grad output.
# Note that because forward_input is captured and not a loop var, its incoming
# gradient should always be zero.
init_slices = _create_grad_indexed_slices_init(grad_output_slices,
                                               forward_input)

# Create a new version of grad_output_slices's gradient computation that uses
# the new IndexedSlices input instead of the original Tensor input. We'll
# return the new computation and leave the old computation as dead code.
# TODO(skyewm): considering pruning body_grad_graph to remove the old
# computation.
with body_grad_graph.as_default():
    input_slices = indexed_slices.IndexedSlices(
        values=body_grad_graph.capture(init_slices.values, allowlisted=True),
        indices=body_grad_graph.capture(init_slices.indices, allowlisted=True),
        dense_shape=body_grad_graph.capture(
            init_slices.dense_shape, allowlisted=True))

    # Remove the captured tensors from the function inputs. We'll add them back
    # at the correct index in _update_indexed_slices_param.
    for t in _flatten(init_slices):
        captured_t = body_grad_graph.captures.pop(t)
        body_grad_graph.inputs.remove(captured_t)

    new_output_slices = _rewrite_grad_indexed_slices_output(
        grad_output_slices, input_slices)

# Update body_grad_graph's inputs and outputs to reflect the new
# IndexedSlices computation.
exit(_update_indexed_slices_param(body_grad_graph, loop_vars, init_slices,
                                    input_slices, new_output_slices,
                                    grad_output_slices))
