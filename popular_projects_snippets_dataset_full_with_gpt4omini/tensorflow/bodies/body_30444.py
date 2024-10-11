# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
with test_util.use_gpu():
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "Dimension must be 2 but is 1|"
                                "paddings must be a matrix with 2 columns"):
        array_ops.pad(array_ops.reshape(
            [1, 2], shape=[1, 2]),
                      array_ops.reshape(
                          [1, 2], shape=[2, 1]))
