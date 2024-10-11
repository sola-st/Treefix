# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
with test_util.use_gpu():
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "Shape must be rank 1 but is rank 2|"
                                "paddings must be the rank of inputs"):
        array_ops.pad(array_ops.reshape(
            [1, 2], shape=[1, 2]),
                      array_ops.reshape(
                          [1, 2], shape=[1, 2]))
