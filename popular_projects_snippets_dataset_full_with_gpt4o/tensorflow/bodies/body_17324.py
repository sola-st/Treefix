# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img = self._LoadTestImages()[:2]
expected = self._ssim[:2, :2]

img = constant_op.constant(np.concatenate(img))
img1 = array_ops.expand_dims(img, axis=0)  # batch dims: 1, 2.
img2 = array_ops.expand_dims(img, axis=1)  # batch dims: 2, 1.

ssim = image_ops.ssim(
    img1, img2, 1.0, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03)
with self.cached_session():
    self.assertAllClose(expected, self.evaluate(ssim), atol=1e-4)
