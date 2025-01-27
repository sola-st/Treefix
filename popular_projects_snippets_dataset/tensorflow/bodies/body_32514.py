# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.cached_session():
    tensor = constant_op.constant(
        [1, 2], dtype=dtypes.float32, name="my_tensor")
    rank_tensor = array_ops.placeholder(dtypes.int32, name="rank_tensor")
    with self.assertRaisesOpError("Rank must be a scalar"):
        with ops.control_dependencies(
            [check_ops.assert_rank(tensor, rank_tensor)]):
            array_ops.identity(tensor).eval(feed_dict={rank_tensor: [1, 2]})
