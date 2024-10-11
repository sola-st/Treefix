# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default():
    c = constant_op.constant_v1([1, 2, 3, 4, 5, 6, 7], shape=[10])
self.assertEqual(c.get_shape(), [10])

with ops.Graph().as_default():
    with self.assertRaisesRegex(TypeError, "Expected Tensor's shape"):
        c = constant_op.constant([1, 2, 3, 4, 5, 6, 7], shape=[10])
