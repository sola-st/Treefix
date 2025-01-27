# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the TensorShape of this tensor according to the C API."""
with self._op._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    shape_vec, unknown_shape = pywrap_tf_session.TF_GraphGetTensorShapeHelper(
        c_graph, self._as_tf_output())
if unknown_shape:
    exit(tensor_shape.unknown_shape())
else:
    shape_vec = [None if d == -1 else d for d in shape_vec]
    exit(tensor_shape.TensorShape(shape_vec))
