# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_ans = np.where(c, x, y)
with test_util.device(use_gpu=use_gpu):
    out = fn(c, x, y)
    tf_ans = self.evaluate(out)
self.assertAllEqual(np_ans, tf_ans)
self.assertShapeEqual(np_ans, out)
