# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/stack_op_test.py
with self.session():
    # Test using placeholder with a defined shape.
    ph_0 = array_ops.placeholder(dtypes.int32, shape=[])
    result_0 = ops.convert_to_tensor([[0, 0, 0], [0, ph_0, 0], [0, 0, 0]])
    self.assertAllEqual([[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                        result_0.eval(feed_dict={ph_0: 1}))
    self.assertAllEqual([[0, 0, 0], [0, 2, 0], [0, 0, 0]],
                        result_0.eval(feed_dict={ph_0: 2}))

    # Test using placeholder with an undefined shape.
    ph_1 = array_ops.placeholder(dtypes.int32)
    result_1 = ops.convert_to_tensor([[0, 0, 0], [0, ph_1, 0], [0, 0, 0]])
    self.assertAllEqual([[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                        result_1.eval(feed_dict={ph_1: 1}))
    self.assertAllEqual([[0, 0, 0], [0, 2, 0], [0, 0, 0]],
                        result_1.eval(feed_dict={ph_1: 2}))
