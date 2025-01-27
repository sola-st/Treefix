# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.cached_session():
    small = array_ops.placeholder(dtypes.int32, name="small")
    big = array_ops.placeholder(dtypes.int32, name="big")
    with ops.control_dependencies([check_ops.assert_equal(small, big)]):
        out = array_ops.identity(small)
    with self.assertRaisesOpError("small.*big"):
        out.eval(feed_dict={small: [3, 1], big: [4, 2]})
