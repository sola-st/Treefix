# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img1 = self._RandomImage((1, 180, 240, 3), 255)
img2 = self._RandomImage((1, 180, 240, 3), 255)
img1 = constant_op.constant(img1, dtypes.uint8)
img2 = constant_op.constant(img2, dtypes.uint8)
ssim_uint8 = image_ops.ssim_multiscale(
    img1, img2, 255, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03)
img1 = image_ops.convert_image_dtype(img1, dtypes.float32)
img2 = image_ops.convert_image_dtype(img2, dtypes.float32)
ssim_float32 = image_ops.ssim_multiscale(
    img1, img2, 1.0, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03)
with self.cached_session():
    self.assertAllClose(
        self.evaluate(ssim_uint8), self.evaluate(ssim_float32), atol=0.001)
