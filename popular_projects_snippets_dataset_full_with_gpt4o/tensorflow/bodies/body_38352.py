# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
np_ans = self._np_reduce(x, reduction_axes, keepdims)
with self.cached_session() as sess:
    tf_ans = self._tf_reduce(x, reduction_axes, keepdims)
    out = sess.run(tf_ans, feed_dict)
self.assertAllClose(np_ans, out, rtol=rtol, atol=atol)
self.assertShapeEqual(np_ans, tf_ans)
