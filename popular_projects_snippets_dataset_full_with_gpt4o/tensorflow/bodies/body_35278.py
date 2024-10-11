# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
dist = make_categorical([], 5, dtype=dtypes.int32)
self.assertEqual(dist.dtype, dtypes.int32)
self.assertEqual(dist.dtype, dist.sample(5).dtype)
self.assertEqual(dist.dtype, dist.mode().dtype)
dist = make_categorical([], 5, dtype=dtypes.int64)
self.assertEqual(dist.dtype, dtypes.int64)
self.assertEqual(dist.dtype, dist.sample(5).dtype)
self.assertEqual(dist.dtype, dist.mode().dtype)
self.assertEqual(dist.probs.dtype, dtypes.float32)
self.assertEqual(dist.logits.dtype, dtypes.float32)
self.assertEqual(dist.logits.dtype, dist.entropy().dtype)
self.assertEqual(
    dist.logits.dtype, dist.prob(np.array(
        0, dtype=np.int64)).dtype)
self.assertEqual(
    dist.logits.dtype, dist.log_prob(np.array(
        0, dtype=np.int64)).dtype)
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    dist = make_categorical([], 5, dtype=dtype)
    self.assertEqual(dist.dtype, dtype)
    self.assertEqual(dist.dtype, dist.sample(5).dtype)
