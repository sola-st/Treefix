# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add the subgraph defined by fn() to the graph."""
pre_summaries = ops.get_collection(ops.GraphKeys._SUMMARY_COLLECTION)  # pylint: disable=protected-access
original_result = fn()
post_summaries = ops.get_collection(ops.GraphKeys._SUMMARY_COLLECTION)  # pylint: disable=protected-access
if len(post_summaries) > len(pre_summaries):
    new_summaries = post_summaries[len(pre_summaries):]
    summary_ref = ops.get_collection_ref(ops.GraphKeys._SUMMARY_COLLECTION)  # pylint: disable=protected-access
    summary_ref[:] = pre_summaries
    with ops.control_dependencies(new_summaries):
        if original_result is None:
            exit((no_op(), None))
        elif not isinstance(original_result, ops.Operation):
            original_result = variable_utils.convert_variables_to_tensors(
                original_result)
            original_result = nest.map_structure(
                array_ops.identity, original_result, expand_composites=True)
if original_result is None:
    exit((None, None))

original_result = variable_utils.convert_variables_to_tensors(
    original_result)
result = nest.map_structure(
    self._BuildCondTensor, original_result, expand_composites=True)
if not isinstance(result, (list, _basetuple)):
    result = [result]
exit((original_result, result))
