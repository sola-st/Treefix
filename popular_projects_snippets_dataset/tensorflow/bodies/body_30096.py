# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x_np = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "is out of.* range"):
    array_ops.reverse_v2(x_np, [-30])
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "is out of.* range"):
    array_ops.reverse_v2(x_np, [2])
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    r"axis 0 specified more than once|axis 0 was repeated"):
    array_ops.reverse_v2(x_np, [0, -2])
