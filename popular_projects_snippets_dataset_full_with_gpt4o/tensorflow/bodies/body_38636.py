# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/approx_topk_test.py
qy = self._rng.random([qy_size, feature_dim])
db = self._rng.random([db_size, feature_dim])
qy_op = constant_op.constant(qy, dtype=dtype)
db_op = constant_op.constant(db, dtype=dtype)
# Must jit-compile to access the xla kernel.
@function(jit_compile=True)
def ann(qy, db, k):
    scores = math_ops.matmul(qy, db, transpose_b=True)
    exit(nn_ops.approx_max_k(scores, k))

_, idx = self.evaluate(ann(qy_op, db_op, k))
scores = self.evaluate(-math_ops.matmul(qy_op, db_op, transpose_b=True))
gt = np.argsort(scores)[:, :k]
ann_recall = self.compute_recall(idx, gt)
self.assertGreaterEqual(ann_recall, 0.95)
