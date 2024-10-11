# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.session(force_gpu=test_util.is_gpu_available()):
    p = array_ops.placeholder_with_default([1, 2, 3], shape=[None])
    a = array_ops.identity(p)
    self.assertAllEqual([1, 2, 3], self.evaluate(a))
    self.assertAllEqual([3, 37], a.eval(feed_dict={p: [3, 37]}))

    with self.assertRaises(ValueError):
        a.eval(feed_dict={p: [[2, 2], [2, 2]]})
