# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
image1 = self._RandomImage((10, 8, 8, 1), 1)
image2 = self._RandomImage((10, 8, 8, 1), 1)
psnr = self._PSNR_NumPy(image1, image2, 1)

with self.cached_session():
    tf_image1 = constant_op.constant(image1, shape=image1.shape,
                                     dtype=dtypes.float32)
    tf_image2 = constant_op.constant(image2, shape=image2.shape,
                                     dtype=dtypes.float32)
    tf_psnr = self.evaluate(image_ops.psnr(tf_image1, tf_image2, 1, "psnr"))
    self.assertAllClose(psnr, tf_psnr, atol=0.001)
