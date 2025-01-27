# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(ValueError, "Too many elements provided."):
        constant_op.constant_v1([1, 2, 3, 4, 5, 6, 7], shape=[5])
    with self.assertRaisesRegex(TypeError, "Expected Tensor's shape"):
        constant_op.constant([1, 2, 3, 4, 5, 6, 7], shape=[5])
