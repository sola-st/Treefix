# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
"""Rewrites grad_output_slices to be a Tensor output.

  Args:
    body_grad_graph: _WhileBodyGradFuncGraph.
    grad_output_slices: IndexedSlices output of body_grad_graph.
  """
with body_grad_graph.as_default():
    new_output = ops.convert_to_tensor_v2(grad_output_slices)

idx = _get_tensor_index_in_iterable(body_grad_graph.structured_outputs,
                                    grad_output_slices)
body_grad_graph.structured_outputs[idx] = new_output
body_grad_graph.outputs = func_graph.flatten(
    body_grad_graph.structured_outputs)
