# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
# tf.parallel_stack is only supported in graph mode.
with ops.Graph().as_default():
    with test_util.device(use_gpu=False):
        t = [constant_op.constant([1, 2, 3]), constant_op.constant([4, 5, 6])]
        stacked = self.evaluate(array_ops.stack(t))
        parallel_stacked = self.evaluate(array_ops.parallel_stack(t))

    expected = np.array([[1, 2, 3], [4, 5, 6]])
    self.assertAllEqual(stacked, expected)
    self.assertAllEqual(parallel_stacked, expected)
