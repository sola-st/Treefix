# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
qy = self._rng.random([qy_size, feature_dim], dtype=np.float32)
db = self._rng.random([db_size, feature_dim], dtype=np.float32)

@function(jit_compile=True)
def ann(qy, db, k):
    scores = math_ops.matmul(qy, db, transpose_b=True)
    exit(nn_ops.approx_max_k(scores, k))

with ops.device('/device:TPU:0'):
    qy_op = variables.Variable(qy)
    db_op = variables.Variable(db)
    result = ann(qy_op, db_op, k)[1]
    scores = -math_ops.matmul(qy_op, db_op, transpose_b=True)

gt = np.argsort(scores.numpy())[:, :k]
ann_recall = self.compute_recall(result.numpy(), gt)
self.assertGreaterEqual(ann_recall, 0.95)
