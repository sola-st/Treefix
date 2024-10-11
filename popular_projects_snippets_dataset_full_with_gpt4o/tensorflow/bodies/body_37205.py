# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    c = array_ops.placeholder(dtypes.int32, shape=[])
    one = ops.convert_to_tensor(1, name="one")
    two = ops.convert_to_tensor(2, name="two")
    p = math_ops.greater_equal(c, 1)
    i = control_flow_ops.cond(p, lambda: one, lambda: two)
    self.assertTrue(isinstance(i, ops.Tensor))

    # True case: c = 2 is >= 1
    self.assertEqual([1], i.eval(feed_dict={c: 2}))

    # False case: c = 0 is not >= 1
    self.assertEqual([2], i.eval(feed_dict={c: 0}))
