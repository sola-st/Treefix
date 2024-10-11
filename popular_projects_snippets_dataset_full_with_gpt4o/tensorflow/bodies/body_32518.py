# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.cached_session():
    tensor_rank0 = array_ops.placeholder(dtypes.float32, name="my_tensor")
    with ops.control_dependencies([
        check_ops.assert_rank_in(tensor_rank0, (1, 2), message="fail")]):
        with self.assertRaisesOpError("fail.*my_tensor.*rank"):
            array_ops.identity(tensor_rank0).eval(feed_dict={tensor_rank0: 42.0})
