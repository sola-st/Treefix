# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/in_topk_op_test.py
np_ans = np.array(expected, np.bool_)
with self.cached_session():
    precision = nn_ops.in_top_k(predictions, target, k)
    out = self.evaluate(precision)
    self.assertAllClose(np_ans, out)
    self.assertShapeEqual(np_ans, precision)
