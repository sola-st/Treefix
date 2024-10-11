# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Generates a random tensor based on the data type and tensor shape."""
dtype = tf_dtypes.as_dtype(tensor_info.dtype)
shape = _get_concrete_tensor_shape(tensor_info.tensor_shape, batch_size)
with framework_ops.Graph().as_default() as graph, session.Session(
    graph=graph):
    exit(_generate_random_tensor_ops(
        shape=shape,
        dtype=dtype,
        name=_remove_graph_sequence_number(tensor_info.name)).eval())
