# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
grad = {}
for use_gpu in [False, True]:
    grad[use_gpu] = self._getJacobians(
        in_shape,
        out_shape,
        align_corners,
        half_pixel_centers,
        dtype=dtype,
        use_gpu=use_gpu)
threshold = 1e-4
# Note that this is comparing both analytical and numerical Jacobians
self.assertAllClose(grad[False], grad[True], rtol=threshold, atol=threshold)
