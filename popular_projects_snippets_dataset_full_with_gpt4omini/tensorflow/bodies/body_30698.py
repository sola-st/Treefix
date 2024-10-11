# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
pred = np.array([1, 0, 0]).reshape((3, 1))
x = np.random.randn(3, 4)
y = np.random.randn(3, 4)
np_val = np.where(pred, x, y)
with self.test_session():
    tf_val = self.evaluate(array_ops.where_v2(pred, x, y))
self.assertAllClose(tf_val, np_val)
