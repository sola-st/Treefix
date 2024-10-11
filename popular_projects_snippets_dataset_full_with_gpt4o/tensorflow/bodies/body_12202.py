# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
"""Handles special case of IndexedSlices returned from while gradient.

  Some gradient functions return IndexedSlices instead of a Tensor (e.g. the
  gradient of Gather ops). When this happens in the gradient of a while body,
  the resulting gradient body function will have mismatched inputs and outputs,
  since the input is a single Tensor, but the IndexedSlices gets unnested into
  three output Tensors.

  This function fixes this by rewriting the gradient body to have three inputs
  to match the three outputs, i.e., it effectively converts the input Tensor
  into an input IndexedSlices. It also returns new `loop_vars` to reflect the
  new inputs.

  Args:
    grads: the input gradient Tensors to the while gradient computation.
    body_grad_graph: _WhileBodyGradFuncGraph.
    loop_vars: list of Tensors. The inputs to body_grad_graph.
    forward_inputs: list of Tensors. The (flat) inputs to the forward-pass While
      op.

  Returns:
    The new loop_vars to pass to body_grad_graph.
  """
# Match up body_grad_graph.structured_outputs with the corresponding
# forward_inputs.
#
# Note that we don't expect a gradient computation to have structured output
# (e.g. no nested lists), so no need to flatten
# body_grad_graph.structured_outputs. However, structured_outputs may still
# contain composite tensors such as IndexedSlices, unlike
# body_grad_graph.outputs, which contains flattened composite tensors.
inputs_with_grads = [
    t for g, t in zip(grads, forward_inputs) if g is not None
]
# Skip loop counter, maximum_iterations and total number of loop iterations.
structured_outputs = body_grad_graph.structured_outputs[3:]

for forward_input, output in zip(inputs_with_grads, structured_outputs):
    if not isinstance(output, indexed_slices.IndexedSlices):
        continue

    if forward_input.dtype == dtypes.resource:
        # TODO(skyewm): In theory we should use this for all captured inputs, not
        # just resource handles (which can only be captured). We can do this by
        # checking that forward_input is passed straight through to its output.
        loop_vars = _rewrite_input_as_indexed_slices(body_grad_graph, output,
                                                     forward_input, loop_vars)
    else:
        _rewrite_output_as_tensor(body_grad_graph, output)

exit(loop_vars)
