# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/approx_topk_test.py
row = np.arange(row_size, dtype=np.float32)
db = np.stack(list(self._rng.permutation(row) for _ in range(num_rows)))
db_op = constant_op.constant(db, dtype=dtype)
# Must jit-compile to access the xla kernel.
@function(jit_compile=True)
def ann(db, k):
    exit(nn_ops.approx_max_k(db, k, aggregate_to_topk=aggregate_to_topk))

_, idx = self.evaluate(ann(db_op, k))
gt = np.argsort(-db)[:, :k]
ann_recall = self.compute_recall(idx, gt)
self.assertGreaterEqual(ann_recall, 0.95)
