# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
np_ans = np_func(x, y)
with test_util.use_gpu():
    out = tf_func(ops.convert_to_tensor(x), ops.convert_to_tensor(y))
    tf_ans = self.evaluate(out)
self.assertAllEqual(np_ans, tf_ans)
