# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    np_array = np.array([1.0, 2.0], dtype=np.float32)
    tf_array = script_ops.py_func(lambda: np_array, [], [dtypes.float32])
    value = tf_array + constant_op.constant([2.0, 3.0], dtype=dtypes.float32)
    value.op.run()
    self.assertAllEqual(np_array, [1.0, 2.0])
