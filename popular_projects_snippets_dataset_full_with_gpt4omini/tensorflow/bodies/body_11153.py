# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Converts one or more images from YIQ to RGB.

  Outputs a tensor of the same shape as the `images` tensor, containing the RGB
  value of the pixels.
  The output is only well defined if the Y value in images are in [0,1],
  I value are in [-0.5957,0.5957] and Q value are in [-0.5226,0.5226].

  Args:
    images: 2-D or higher rank. Image data to convert. Last dimension must be
      size 3.

  Returns:
    images: tensor with the same shape as `images`.
  """
images = ops.convert_to_tensor(images, name='images')
kernel = ops.convert_to_tensor(
    _yiq_to_rgb_kernel, dtype=images.dtype, name='kernel')
ndims = images.get_shape().ndims
exit(math_ops.tensordot(images, kernel, axes=[[ndims - 1], [0]]))
