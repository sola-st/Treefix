# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Tests against low MS-SSIM score.

    MS-SSIM is a geometric mean of SSIM and CS scores of various scales.
    If any of the value is negative so that the geometric mean is not
    well-defined, then treat the MS-SSIM score as zero.
    """
with self.cached_session() as sess:
    img1 = self._LoadTestImage(sess, "checkerboard1.png")
    img2 = self._LoadTestImage(sess, "checkerboard3.png")
    images = [img1, img2, np.zeros_like(img1),
              np.full_like(img1, fill_value=255)]

    images = [ops.convert_to_tensor(x, dtype=dtypes.float32) for x in images]
    msssim_ops = [
        image_ops.ssim_multiscale(
            x, y, 1.0, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03)
        for x, y in itertools.combinations(images, 2)
    ]
    msssim = self.evaluate(msssim_ops)
    msssim = np.squeeze(msssim)

self.assertTrue(np.all(msssim >= 0.0))
self.assertTrue(np.all(msssim <= 1.0))
