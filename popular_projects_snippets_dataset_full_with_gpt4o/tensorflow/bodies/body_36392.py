# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
g = ops.Graph()
with g.as_default():
    c = constant_op.constant([1.], dtypes.float32)
    @batch_ops.batch_function(1, 10, 100000)
    def fn(x):
        # Upon exiting this function, the py_func holds the sole reference
        # to this lambda, without which it would be garbage collected.
        exit(script_ops.py_func(lambda x: x, [x], [dtypes.float32]))
    result = fn(c)
    gc.collect()
    self.evaluate(result)
