# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
q20, q72, q95 = self._LoadTestImages()

# Verify NumPy implementation first.
# Golden values are generated using GNU Octave's psnr() function.
psnr1 = self._PSNR_NumPy(q20, q72, 1)
self.assertNear(30.321, psnr1, 0.001, msg="q20.dtype=" + str(q20.dtype))
psnr2 = self._PSNR_NumPy(q20, q95, 1)
self.assertNear(29.994, psnr2, 0.001)
psnr3 = self._PSNR_NumPy(q72, q95, 1)
self.assertNear(35.302, psnr3, 0.001)

# Test TensorFlow implementation.
with self.cached_session():
    tf_q20 = constant_op.constant(q20, shape=q20.shape, dtype=dtypes.float32)
    tf_q72 = constant_op.constant(q72, shape=q72.shape, dtype=dtypes.float32)
    tf_q95 = constant_op.constant(q95, shape=q95.shape, dtype=dtypes.float32)
    tf_psnr1 = self.evaluate(image_ops.psnr(tf_q20, tf_q72, 1, "psnr1"))
    tf_psnr2 = self.evaluate(image_ops.psnr(tf_q20, tf_q95, 1, "psnr2"))
    tf_psnr3 = self.evaluate(image_ops.psnr(tf_q72, tf_q95, 1, "psnr3"))
    self.assertAllClose(psnr1, tf_psnr1, atol=0.001)
    self.assertAllClose(psnr2, tf_psnr2, atol=0.001)
    self.assertAllClose(psnr3, tf_psnr3, atol=0.001)
