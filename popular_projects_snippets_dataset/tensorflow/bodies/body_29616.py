# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
x = array_ops.zeros(shape=(0, 1, 2))
y = self.evaluate(array_ops.unstack(x, axis=1)[0])
self.assertEqual(y.shape, (0, 2))
