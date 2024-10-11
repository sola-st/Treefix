# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
image = np.arange(48, dtype=np.uint8).reshape([2, 2, 4, 3])
with self.cached_session():
    for k in range(4):
        y_np = np.rot90(image, k=k, axes=(1, 2))
        self.assertAllEqual(
            y_np, self.evaluate(image_ops.rot90(image, k)))
