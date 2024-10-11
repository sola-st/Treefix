# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session() as sess:
    x = array_ops.zeros([1000000], dtype=np.float32)
    y = script_ops.py_func(lambda x: x + 1, [x], [dtypes.float32])
    z = script_ops.py_func(lambda x: x * 2, [x], [dtypes.float32])
    for _ in range(100):
        sess.run([y[0].op, z[0].op])
