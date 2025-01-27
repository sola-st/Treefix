# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.session(force_gpu=test_util.is_gpu_available()):
    p = array_ops.placeholder_with_default([[2, 2], [2, 2]], shape=[2, 2])
    a = array_ops.identity(p)
    self.assertAllEqual([[2, 2], [2, 2]], self.evaluate(a))
    self.assertAllEqual(
        [[3, 3], [3, 3]], a.eval(feed_dict={p: [[3, 3], [3, 3]]}))

    with self.assertRaises(ValueError):
        a.eval(feed_dict={p: [[6, 6, 6], [6, 6, 6]]})
