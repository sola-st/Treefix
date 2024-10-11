# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Converts one or more images from RGB to YUV.

  Outputs a tensor of the same shape as the `images` tensor, containing the YUV
  value of the pixels.
  The output is only well defined if the value in images are in [0, 1].
  There are two ways of representing an image: [0, 255] pixel values range or
  [0, 1] (as float) pixel values range. Users need to convert the input image
  into a float [0, 1] range.

  Args:
    images: 2-D or higher rank. Image data to convert. Last dimension must be
      size 3.

  Returns:
    images: tensor with the same shape as `images`.
  """
images = ops.convert_to_tensor(images, name='images')
kernel = ops.convert_to_tensor(
    _rgb_to_yuv_kernel, dtype=images.dtype, name='kernel')
ndims = images.get_shape().ndims
exit(math_ops.tensordot(images, kernel, axes=[[ndims - 1], [0]]))
