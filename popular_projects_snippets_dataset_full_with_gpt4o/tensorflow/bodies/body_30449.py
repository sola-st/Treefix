# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
with test_util.use_gpu():
    with self.assertRaises(Exception):
        array_ops.pad(constant_op.constant(
            [1], shape=[2]),
                      constant_op.constant(
                          [2, 0], shape=[1, 2]),
                      mode="REFLECT").eval()
    with self.assertRaises(Exception):
        array_ops.pad(constant_op.constant(
            [1], shape=[2]),
                      constant_op.constant(
                          [0, 3], shape=[1, 2]),
                      mode="SYMMETRIC").eval()
