# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
# Use the new rng api
row = np.arange(row_size, dtype=np.float32)
db = np.stack(list(self._rng.permutation(row) for _ in range(num_rows)))

@function(jit_compile=True)
def ann(db, k=10):
    exit(nn_ops.approx_min_k(db, k, aggregate_to_topk=aggregate_to_topk))

with ops.device('/device:TPU:0'):
    db_op = variables.Variable(db)
    result = ann(db_op, k)[1]

gt = np.argsort(db)[:, :k]
ann_recall = self.compute_recall(result.numpy(), gt)
self.assertGreaterEqual(ann_recall, 0.95)
