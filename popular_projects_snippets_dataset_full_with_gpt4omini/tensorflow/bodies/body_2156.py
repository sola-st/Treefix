# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
qy = self._rng.random([qy_size, feature_dim], dtype=np.float32)
db = self._rng.random([db_size, feature_dim], dtype=np.float32)
db_half_norm_sq = np.linalg.norm(db, axis=1)**2 / 2

@function(jit_compile=True)
def ann(qy, db, db_half_norm_sq, k):
    scores = db_half_norm_sq - math_ops.matmul(qy, db, transpose_b=True)
    exit(nn_ops.approx_min_k(scores, k))

with ops.device('/device:TPU:0'):
    qy_op = variables.Variable(qy)
    db_op = variables.Variable(db)
    db_half_norm_sq_op = variables.Variable(db_half_norm_sq)
    result = ann(qy_op, db_op, db_half_norm_sq_op, k)[1]
    scores = db_half_norm_sq_op - math_ops.matmul(
        qy_op, db_op, transpose_b=True)

gt = np.argsort(scores.numpy())[:, :k]
ann_recall = self.compute_recall(result.numpy(), gt)
self.assertGreaterEqual(ann_recall, 0.95)
