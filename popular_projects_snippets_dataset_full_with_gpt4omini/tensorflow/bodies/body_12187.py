# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clip_ops_test.py
clipped = clip_ops.clip_by_global_norm(inputs, max_norm)
result, _ = self.evaluate(clipped)
self.assertAllClose(result, expected)
