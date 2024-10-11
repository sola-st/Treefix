# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x = np.ndarray(shape=[0, 1, 1])
v = array_ops.reverse_v2(x, axis=[1])
self.assertAllEqual(self.evaluate(v), v)
