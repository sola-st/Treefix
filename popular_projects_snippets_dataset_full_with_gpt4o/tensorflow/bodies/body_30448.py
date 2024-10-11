# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
with test_util.use_gpu():
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "must be non-negative"):
        array_ops.pad(constant_op.constant(
            [1], shape=[1]),
                      constant_op.constant(
                          [-1, 0], shape=[1, 2]))
