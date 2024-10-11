# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tensor = constant_op.constant((42, 43), name="my_tensor")
desired_ranks = (
    np.array(1, dtype=np.int32),
    np.array((2, 1), dtype=np.int32))
with self.assertRaisesRegex(ValueError, "Rank must be a scalar"):
    check_ops.assert_rank_in(tensor, desired_ranks)
