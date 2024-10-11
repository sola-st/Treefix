# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
y = constant_op.constant(0.0, shape=[23, 29, 31])
with self.assertRaisesRegex(ValueError, "must be evenly divisible by 17"):
    array_ops.reshape(y, [17, -1])

z = constant_op.constant(0.0, shape=[32, 128])
with self.assertRaisesRegex(ValueError,
                            "Cannot reshape a tensor with 4096 elements"):
    array_ops.reshape(z, [4095])
