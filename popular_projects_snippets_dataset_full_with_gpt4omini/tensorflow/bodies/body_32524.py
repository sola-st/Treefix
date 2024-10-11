# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.cached_session():
    tensor_rank1 = array_ops.placeholder(dtypes.float32, name="my_tensor")
    with ops.control_dependencies([
        check_ops.assert_rank_in(tensor_rank1, (0, 2))]):
        with self.assertRaisesOpError("my_tensor.*rank"):
            array_ops.identity(tensor_rank1).eval(feed_dict={
                tensor_rank1: (42.0, 43.0)
            })
