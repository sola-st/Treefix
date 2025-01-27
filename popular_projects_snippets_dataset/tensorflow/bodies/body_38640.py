# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/approx_topk_test.py
db = self._rng.random([2, 10, 200, 3], dtype=np.float32)
k = 5

@function(jit_compile=True)
def ann(db, k):
    exit(nn_ops.approx_min_k(db, k=k, reduction_dimension=2))

_, idx = self.evaluate(ann(db, k))
gt = np.argsort(db, axis=2)[:, :, :k, :]
flat_idx = np.reshape(np.transpose(idx, [0, 1, 3, 2]), [2 * 10 * 3, k])
flat_gt = np.reshape(np.transpose(gt, [0, 1, 3, 2]), [2 * 10 * 3, k])
ann_recall = self.compute_recall(flat_idx, flat_gt)
self.assertGreaterEqual(ann_recall, 0.95)
