# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.cached_session():
    tensor_rank0 = array_ops.placeholder(dtypes.float32, name="my_tensor")
    for desired_ranks in ((0, 1, 2), (1, 0, 2), (1, 2, 0)):
        with ops.control_dependencies([
            check_ops.assert_rank_in(tensor_rank0, desired_ranks)]):
            array_ops.identity(tensor_rank0).eval(feed_dict={tensor_rank0: 42.0})
