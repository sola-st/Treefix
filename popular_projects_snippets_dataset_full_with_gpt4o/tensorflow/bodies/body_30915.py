# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
x = array_ops.ones(shape=[0, 3], dtype=dtypes.float32)
y = np.zeros(shape=[0, 3], dtype=np.float32)
self.assertEqual(0, self.evaluate(array_ops.size(x)))
self.assertAllEqual(y, self.evaluate(nn_ops.softmax(x, axis=0)))
