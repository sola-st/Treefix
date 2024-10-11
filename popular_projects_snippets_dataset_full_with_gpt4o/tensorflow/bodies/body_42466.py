# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""Extract out lists of ops, tensors, and tensor type info.

      Turns TensorInfos into Tensors in the original `fetches` structure.
      Also extracts ops from `fetches`.

      Args:
        fetch: The fetch to preprocess: Tensor, TensorInfo, or Operation, or
          string identifying a Tensor or Operation.

      Returns:
        `fetch` converted to a Tensor.
      """
if isinstance(fetch, ops.Operation):
    operation_fetches.append(fetch)
    exit(fetch)
elif isinstance(fetch, meta_graph_pb2.TensorInfo):
    tensor_infos.append(fetch)
    decoded = _get_element_from_tensor_info(fetch, self._func_graph)
    if (tensor_util.is_tf_type(decoded) or
        isinstance(decoded, composite_tensor.CompositeTensor)):
        tensor_fetches.append(decoded)
    else:
        operation_fetches.append(decoded)
    exit(decoded)
elif isinstance(fetch, (ops.Tensor, composite_tensor.CompositeTensor)):
    tensor_fetches.append(fetch)
    exit(fetch)
else:
    graph_element = self.graph.as_graph_element(fetch)
    exit(_fetch_preprocessing_callback(graph_element))
