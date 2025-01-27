# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_ans = np.dstack(
    [x_i if c_i else y_i for c_i, x_i, y_i in zip(c, x, y)]).transpose(
        [2, 0, 1])
with test_util.device(use_gpu=use_gpu):
    out = array_ops.where(c, x, y)
    tf_ans = self.evaluate(out)
self.assertAllEqual(np_ans, tf_ans)
self.assertShapeEqual(np_ans, out)
