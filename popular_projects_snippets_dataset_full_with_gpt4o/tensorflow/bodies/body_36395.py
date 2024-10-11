# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def make_graph():
    g = ops.Graph()
    with g.as_default():
        c = constant_op.constant([1.], dtypes.float32)
        _ = script_ops.py_func(lambda x: x + 1, [c], [dtypes.float32])
        _ = script_ops.eager_py_func(lambda x: x + 1, [c], [dtypes.float32])
        # These ops have a reference to 'c' which has a reference to the
        # graph.
        # Checks if the functions are being deleted though the graph is
        # referenced from them (see #18292).
        script_ops.py_func(
            lambda x: x + c.shape[0], [c], [dtypes.float32])
        script_ops.eager_py_func(
            lambda x: x + c.shape[0], [c], [dtypes.float32])

self.verifyPyFuncsNoIncrease(make_graph)
