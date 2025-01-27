# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Returns the values that should be returned from the while grad function.

  Args:
    outputs: the raw Tensor outputs of the grad While op.
    grads: the input gradients to the gradient function.
    body_grad_graph: _WhileBodyGradFuncGraph.

  Returns:
    A list of gradient values. May include Nones.
  """
result = []
# outputs[0] is the loop counter.
# outputs[1] is maximum_iterations.
# outputs[2] is the total number of loop iterations.
outputs_idx = 3
structured_outputs_idx = 3
for g in grads:
    # Set None as the output gradient for tensors with None input gradient.
    if g is None:
        result.append(None)
        continue
    output = body_grad_graph.structured_outputs[structured_outputs_idx]
    structured_outputs_idx += 1
    if isinstance(output, indexed_slices.IndexedSlices):
        # TODO(skyewm): is there a more robust way to determine the order of
        # flattened IndexedSlices components?
        result.append(indexed_slices.IndexedSlices(
            values=outputs[outputs_idx],
            indices=outputs[outputs_idx + 1],
            dense_shape=outputs[outputs_idx + 2]))
        outputs_idx += 3
    else:
        assert isinstance(output, ops.Tensor)
        result.append(outputs[outputs_idx])
        outputs_idx += 1

exit(result)
