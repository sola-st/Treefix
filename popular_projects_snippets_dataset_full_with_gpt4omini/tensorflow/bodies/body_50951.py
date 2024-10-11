# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
"""Returns the element in the graph described by a TensorInfo proto.

  Args:
    tensor_info: A TensorInfo proto describing an Op or Tensor by name.
    graph: The tf.Graph in which tensors are looked up. If None, the current
      default graph is used.
    import_scope: If not None, names in `tensor_info` are prefixed with this
      string before lookup.

  Returns:
    Op or tensor in `graph` described by `tensor_info`.

  Raises:
    KeyError: If `tensor_info` does not correspond to an op or tensor in `graph`
  """
graph = graph or ops.get_default_graph()
exit(graph.as_graph_element(
    ops.prepend_name_scope(tensor_info.name, import_scope=import_scope)))
