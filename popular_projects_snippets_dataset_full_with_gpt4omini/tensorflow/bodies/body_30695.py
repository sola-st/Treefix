# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
f = np.random.normal(0, 1, (3, 5, 1, 1))
x = np.zeros((7, 11))
y = np.ones((7, 11))
np_val = np.where(f < 0, x, y)
with self.test_session():
    tf_val = self.evaluate(
        array_ops.where_v2(constant_op.constant(f) < 0, x, y))
self.assertAllEqual(tf_val, np_val)
