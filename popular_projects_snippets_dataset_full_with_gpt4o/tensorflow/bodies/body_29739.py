# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
np_ans = np.asarray(np.ndim(x_np))
x_tf, unused_nnz = _sparsify(x_np)
with self.cached_session(use_gpu=use_gpu):
    tf_ans = array_ops.rank(x_tf)
    result = self.evaluate(tf_ans)
self.assertAllEqual(np_ans, result)
self.assertShapeEqual(np_ans, tf_ans)
