# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
k = 1

row_size = 100
num_rows = 10

row = np.arange(row_size, dtype=np.float32)
db1 = np.stack(list(self._rng.permutation(row) for _ in range(num_rows)))
db2 = np.stack(list(self._rng.permutation(row) for _ in range(num_rows)))

@function(jit_compile=True)
def ann(db1, db2):
    result1 = nn_ops.approx_max_k(db1, k, aggregate_to_topk=True)
    result2 = nn_ops.approx_max_k(db2, k, aggregate_to_topk=True)
    exit((result1, result2))

with ops.device('/device:TPU:0'):
    db1_op = variables.Variable(db1)
    db2_op = variables.Variable(db2)
    result1, result2 = ann(db1_op, db2_op)

gt = np.argsort(-db1)[:, :k]
ann_recall = self.compute_recall(result1[1].numpy(), gt)
self.assertGreaterEqual(ann_recall, 0.95)

gt = np.argsort(-db2)[:, :k]
ann_recall = self.compute_recall(result2[1].numpy(), gt)
self.assertGreaterEqual(ann_recall, 0.95)
