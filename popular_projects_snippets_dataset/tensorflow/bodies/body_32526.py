# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.cached_session():
    tensor = constant_op.constant(
        (42, 43), dtype=dtypes.float32, name="my_tensor")
    desired_ranks = (
        array_ops.placeholder(dtypes.int32, name="rank0_tensor"),
        array_ops.placeholder(dtypes.int32, name="rank1_tensor"))
    with self.assertRaisesOpError("Rank must be a scalar"):
        with ops.control_dependencies(
            (check_ops.assert_rank_in(tensor, desired_ranks),)):
            array_ops.identity(tensor).eval(feed_dict={
                desired_ranks[0]: 1,
                desired_ranks[1]: [2, 1],
            })
