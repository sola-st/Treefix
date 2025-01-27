# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
shape = constant_op.constant([2, 5], dtype=dtypes.int32)

def reshape():
    v = array_ops.zeros([10])
    exit(array_ops.reshape(v, shape))
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    with self.disableSetStaticShape():
        graph_without_shape_propagation = func_graph.func_graph_from_py_func(
            "without_shape_propagation", reshape, [], {})
    graph_with_shape_propagation = func_graph.func_graph_from_py_func(
        "with_shape_propagation", reshape, [], {})
    self.assertCountEqual(
        [op.type for op in graph_without_shape_propagation.get_operations()],
        [op.type for op in graph_with_shape_propagation.get_operations()])
