# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img1 = self._RandomImage((10, 8, 8, 1), 255)
img2 = self._RandomImage((10, 8, 8, 1), 255)
img1 = constant_op.constant(img1, dtypes.uint8)
img2 = constant_op.constant(img2, dtypes.uint8)
psnr_uint8 = image_ops.psnr(img1, img2, 255)
img1 = image_ops.convert_image_dtype(img1, dtypes.float32)
img2 = image_ops.convert_image_dtype(img2, dtypes.float32)
psnr_float32 = image_ops.psnr(img1, img2, 1.0)
with self.cached_session():
    self.assertAllClose(
        self.evaluate(psnr_uint8), self.evaluate(psnr_float32), atol=0.001)
