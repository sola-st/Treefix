# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img1 = self._RandomImage((1, 16, 16, 3), 255)
img2 = self._RandomImage((1, 16, 16, 3), 255)

ssim_locals = image_ops.ssim(
    img1,
    img2,
    1.0,
    filter_size=11,
    filter_sigma=1.5,
    k1=0.01,
    k2=0.03,
    return_index_map=True)
self.assertEqual(ssim_locals.shape, (1, 6, 6))

ssim_global = image_ops.ssim(
    img1, img2, 1.0, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03)

axes = constant_op.constant([-2, -1], dtype=dtypes.int32)
self.assertAllClose(ssim_global, math_ops.reduce_mean(ssim_locals, axes))
