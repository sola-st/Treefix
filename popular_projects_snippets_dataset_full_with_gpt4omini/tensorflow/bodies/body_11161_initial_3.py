filter_size = 11 # pragma: no cover
filter_sigma = 1.5 # pragma: no cover
max_val = 255.0 # pragma: no cover
k1 = 0.01 # pragma: no cover
k2 = 0.03 # pragma: no cover
return_index_map = False # pragma: no cover
_fspecial_gauss = lambda size, sigma: tf.reshape(tf.linalg.band_part(tf.exp(-tf.range(-size//2 + 1, size//2 + 1, dtype=tf.float32)**2 / (2 * sigma**2)), 0, 0), (size, size)) # pragma: no cover
_ssim_helper = lambda img1, img2, reducer, max_val, compensation, k1, k2: (tf.random.uniform(shape=[10], minval=0, maxval=1), tf.random.uniform(shape=[10], minval=0, maxval=1)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
from l3.Runtime import _l_
"""Computes SSIM index between img1 and img2 per color channel.

  This function matches the standard SSIM implementation from:
  Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). Image
  quality assessment: from error visibility to structural similarity. IEEE
  transactions on image processing.

  Details:
    - 11x11 Gaussian filter of width 1.5 is used.
    - k1 = 0.01, k2 = 0.03 as in the original paper.

  Args:
    img1: First image batch.
    img2: Second image batch.
    max_val: The dynamic range of the images (i.e., the difference between the
      maximum the and minimum allowed values).
    filter_size: Default value 11 (size of gaussian filter).
    filter_sigma: Default value 1.5 (width of gaussian filter).
    k1: Default value 0.01
    k2: Default value 0.03 (SSIM is less sensitivity to K2 for lower values, so
      it would be better if we took the values in the range of 0 < K2 < 0.4).
    return_index_map: If True returns local SSIM map instead of the global mean.

  Returns:
    A pair of tensors containing and channel-wise SSIM and contrast-structure
    values. The shape is [..., channels].
  """
filter_size = constant_op.constant(filter_size, dtype=dtypes.int32)
_l_(5500)
filter_sigma = constant_op.constant(filter_sigma, dtype=img1.dtype)
_l_(5501)

shape1, shape2 = array_ops.shape_n([img1, img2])
_l_(5502)
checks = [
    control_flow_ops.Assert(
        math_ops.reduce_all(
            math_ops.greater_equal(shape1[-3:-1], filter_size)),
        [shape1, filter_size],
        summarize=8),
    control_flow_ops.Assert(
        math_ops.reduce_all(
            math_ops.greater_equal(shape2[-3:-1], filter_size)),
        [shape2, filter_size],
        summarize=8)
]
_l_(5503)

# Enforce the check to run before computation.
with ops.control_dependencies(checks):
    _l_(5505)

    img1 = array_ops.identity(img1)
    _l_(5504)

# TODO(sjhwang): Try to cache kernels and compensation factor.
kernel = _fspecial_gauss(filter_size, filter_sigma)
_l_(5506)
kernel = array_ops.tile(kernel, multiples=[1, 1, shape1[-1], 1])
_l_(5507)

# The correct compensation factor is `1.0 - tf.reduce_sum(tf.square(kernel))`,
# but to match MATLAB implementation of MS-SSIM, we use 1.0 instead.
compensation = 1.0
_l_(5508)

# TODO(sjhwang): Try FFT.
# TODO(sjhwang): Gaussian kernel is separable in space. Consider applying
#   1-by-n and n-by-1 Gaussian filters instead of an n-by-n filter.
def reducer(x):
    _l_(5513)

    shape = array_ops.shape(x)
    _l_(5509)
    x = array_ops.reshape(x, shape=array_ops.concat([[-1], shape[-3:]], 0))
    _l_(5510)
    y = nn.depthwise_conv2d(x, kernel, strides=[1, 1, 1, 1], padding='VALID')
    _l_(5511)
    aux = array_ops.reshape(
        y, array_ops.concat([shape[:-3], array_ops.shape(y)[1:]], 0))
    _l_(5512)
    exit(aux)

luminance, cs = _ssim_helper(img1, img2, reducer, max_val, compensation, k1,
                             k2)
_l_(5514)

# Average over the second and the third from the last: height, width.
if return_index_map:
    _l_(5519)

    ssim_val = luminance * cs
    _l_(5515)
else:
    axes = constant_op.constant([-3, -2], dtype=dtypes.int32)
    _l_(5516)
    ssim_val = math_ops.reduce_mean(luminance * cs, axes)
    _l_(5517)
    cs = math_ops.reduce_mean(cs, axes)
    _l_(5518)
aux = (ssim_val, cs)
_l_(5520)
exit(aux)
