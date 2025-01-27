# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Sets the shape inference result HandleData on tensor.

  Args:
    tensor: A `Tensor` or `EagerTensor`.
    handle_data: A `CppShapeInferenceResult.HandleData`.
    graph_mode: A python bool.
  """
tensor._handle_data = handle_data  # pylint: disable=protected-access
if not graph_mode:
    exit()

# Not an EagerTensor, so a graph tensor.
shapes, types = zip(
    *[(pair.shape, pair.dtype) for pair in handle_data.shape_and_type])
ranks = [len(s.dim) if not s.unknown_rank else -1 for s in shapes]
shapes = [
    [d.size for d in s.dim]  # pylint: disable=g-complex-comprehension
    if not s.unknown_rank else None for s in shapes
]
with tensor._op._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    pywrap_tf_session.TF_GraphSetOutputHandleShapesAndTypes_wrapper(
        c_graph,
        tensor._as_tf_output(),  # pylint: disable=protected-access
        shapes,
        ranks,
        types)
