# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py

def reshape():
    v = array_ops.placeholder(dtypes.float32)
    t = array_ops.reshape(v, [-1])
    exit(t)

with self.disableSetStaticShape():
    graph_without_shape_propagation = func_graph.func_graph_from_py_func(
        "without_shape_propagation", reshape, [], {})
graph_with_shape_propagation = func_graph.func_graph_from_py_func(
    "with_shape_propagation", reshape, [], {})
self.assertCountEqual(
    [op.type for op in graph_without_shape_propagation.get_operations()],
    [op.type for op in graph_with_shape_propagation.get_operations()])
