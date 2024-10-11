# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
x = np.zeros(7)
y = np.ones(7)
np_val = np.where([True], x, y)
with self.test_session():
    tf_val = self.evaluate(
        array_ops.where_v2(
            constant_op.constant([True], dtype=dtypes.bool), x, y))
self.assertAllEqual(tf_val, np_val)
