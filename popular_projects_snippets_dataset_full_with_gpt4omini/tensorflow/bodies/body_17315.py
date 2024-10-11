# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
q20, _, _ = self._LoadTestImages()
psnr = self._PSNR_NumPy(q20, q20, 1)
with self.cached_session():
    tf_q20 = constant_op.constant(q20, shape=q20.shape, dtype=dtypes.float32)
    tf_psnr = self.evaluate(image_ops.psnr(tf_q20, tf_q20, 1, "psnr"))
    self.assertAllClose(psnr, tf_psnr, atol=0.001)
