# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
"""Updates graph with new IndexedSlices input/output.

  Updates graph's metadata to output the gradient computation defined by
  init_slices, input_slices, and output_slices, instead of outputting
  old_output_slices. Also returns a new version of loop_vars with init_slices
  replacing the old input.

  Args:
    graph: _WhileBodyGradFuncGraph.
    loop_vars: the inputs to graph.
    init_slices: the new IndexedSlices to use as input to graph.
    input_slices: the new IndexedSlices in graph that should be fed by
      init_slices.
    output_slices: the new IndexedSlices in graph that should be the
      corresponding output to input_slices.
    old_output_slices: the IndexedSlices in graph that are currently being
      output.

  Returns:
    New loop_vars to pass to graph.
  """
structured_idx = _get_tensor_index_in_iterable(graph.structured_outputs,
                                               old_output_slices)
# We assume that the component tensors of old_output_slices appear
# sequentially in graph.outputs. We use the first of these tensors
# as the reference index.
flat_idx = _get_tensor_index_in_iterable(
    graph.outputs,
    func_graph.flatten(old_output_slices)[0])

graph.structured_outputs[structured_idx] = output_slices
graph.outputs = func_graph.flatten(graph.structured_outputs)

graph.inputs = (
    graph.inputs[:flat_idx] + _flatten(input_slices) +
    graph.inputs[flat_idx + 1:])

exit(loop_vars[:flat_idx] + _flatten(init_slices) + loop_vars[flat_idx + 1:])
