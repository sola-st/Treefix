# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Returns the requested return elements from results.

  Args:
    requested_return_elements: list of strings of operation and tensor names
    graph: Graph
    results: wrapped TF_ImportGraphDefResults

  Returns:
    list of `Operation` and/or `Tensor` objects
  """
return_outputs = c_api.TF_ImportGraphDefResultsReturnOutputs(results)
return_opers = c_api.TF_ImportGraphDefResultsReturnOperations(results)

combined_return_elements = []
outputs_idx = 0
opers_idx = 0
for name in requested_return_elements:
    if ':' in name:
        combined_return_elements.append(
            graph._get_tensor_by_tf_output(return_outputs[outputs_idx]))  # pylint: disable=protected-access
        outputs_idx += 1
    else:
        combined_return_elements.append(
            graph._get_operation_by_tf_operation(return_opers[opers_idx]))  # pylint: disable=protected-access
        opers_idx += 1
exit(combined_return_elements)
