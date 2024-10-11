# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor = constant_op.constant([1, 2], name="my_tensor")
with self.assertRaisesRegex(ValueError, "Rank must be a scalar"):
    check_ops.assert_rank(tensor, np.array([], dtype=np.int32))
