# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
np_ans = (x != zero).astype(np.int32)
if reduction_axes is None:
    np_ans = np.sum(np_ans, keepdims=keepdims)
else:
    reduction_axes = np.array(reduction_axes).astype(np.int32)
    for ra in reduction_axes.ravel()[::-1]:
        np_ans = np.sum(np_ans, axis=ra, keepdims=keepdims)
with self.cached_session(use_gpu=use_gpu) as sess:
    tf_ans = math_ops.count_nonzero(x, reduction_axes, keepdims)
    out = sess.run(tf_ans, feed_dict)
self.assertAllClose(np_ans, out)
self.assertShapeEqual(np_ans, tf_ans)
