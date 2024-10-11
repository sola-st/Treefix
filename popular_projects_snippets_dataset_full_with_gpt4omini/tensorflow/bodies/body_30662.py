# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
x = np.array([[-2, 3, -1], [1, -3, -3]])
np_val = np.where(x > 0, x * x, -x)
with self.test_session():
    tf_val = self.evaluate(fn(constant_op.constant(x) > 0, x * x, -x))
self.assertAllEqual(tf_val, np_val)
