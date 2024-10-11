# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Tests against negative SSIM index."""
step = np.expand_dims(np.arange(0, 256, 16, dtype=np.uint8), axis=0)
img1 = np.tile(step, (16, 1))
img2 = np.fliplr(img1)

img1 = img1.reshape((1, 16, 16, 1))
img2 = img2.reshape((1, 16, 16, 1))

ssim = image_ops.ssim(
    constant_op.constant(img1),
    constant_op.constant(img2),
    255,
    filter_size=11,
    filter_sigma=1.5,
    k1=0.01,
    k2=0.03)
with self.cached_session():
    self.assertLess(self.evaluate(ssim), 0)
