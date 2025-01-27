# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [1, 5, 7, 1]
out_shape = [1, 9, 11, 1]
# Note that there is no 16-bit floating-point format registered for GPU
self._gpuVsCpuCase(
    in_shape,
    out_shape,
    align_corners=True,
    half_pixel_centers=False,
    dtype=np.float64)
