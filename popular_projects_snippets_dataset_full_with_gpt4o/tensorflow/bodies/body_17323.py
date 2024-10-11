# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img = self._LoadTestImages()
expected = self._ssim[np.triu_indices(3, k=1)]

img1, img2 = zip(*itertools.combinations(img, 2))
img1 = np.concatenate(img1)
img2 = np.concatenate(img2)

with self.cached_session():
    img1 = self.evaluate(constant_op.constant(img1))
    img2 = self.evaluate(constant_op.constant(img2))

ssim = image_ops.ssim(
    img1,
    img2,
    1.0,
    filter_size=11,
    filter_sigma=1.5,
    k1=0.01,
    k2=0.03)
with self.cached_session():
    self.assertAllClose(expected, self.evaluate(ssim), atol=1e-4)
