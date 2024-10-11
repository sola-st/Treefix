# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.cached_session():
    small = array_ops.placeholder(dtypes.int32, name="small")
    big = array_ops.placeholder(dtypes.int32, name="big")
    with ops.control_dependencies(
        [check_ops.assert_equal(big, small, message="fail")]):
        out = array_ops.identity(small)
    with self.assertRaisesOpError("fail.*big.*small"):
        out.eval(feed_dict={small: [1, 2], big: [3, 4]})
