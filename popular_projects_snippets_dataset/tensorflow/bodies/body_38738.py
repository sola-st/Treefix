# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
empty_image = np.zeros((0, 4, 3, 0))
offsets = np.zeros((0, 2))
with self.cached_session():
    result = image_ops.extract_glimpse(empty_image, [1, 1], offsets)
    self.assertAllEqual(
        np.zeros((0, 1, 1, 0), dtype=np.float32), self.evaluate(result))
