# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.cached_session():
    tensor = array_ops.placeholder(dtypes.float32, name="my_tensor")
    desired_rank = 1
    with ops.control_dependencies(
        [check_ops.assert_rank_at_least(tensor, desired_rank)]):
        array_ops.identity(tensor).eval(feed_dict={tensor: [1, 2]})
