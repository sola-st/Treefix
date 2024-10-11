# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
image = np.arange(24, dtype=np.uint8).reshape([2, 4, 3])
with self.cached_session():
    rotated = image
    for _ in range(4):
        rotated = image_ops.rot90(rotated)
    self.assertAllEqual(image, self.evaluate(rotated))
