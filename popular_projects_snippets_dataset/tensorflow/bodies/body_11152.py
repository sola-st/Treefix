# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Converts one or more images from RGB to YIQ.

  Outputs a tensor of the same shape as the `images` tensor, containing the YIQ
  value of the pixels.
  The output is only well defined if the value in images are in [0,1].

  Usage Example:

  >>> x = tf.constant([[[1.0, 2.0, 3.0]]])
  >>> tf.image.rgb_to_yiq(x)
  <tf.Tensor: shape=(1, 1, 3), dtype=float32,
  numpy=array([[[ 1.815     , -0.91724455,  0.09962624]]], dtype=float32)>

  Args:
    images: 2-D or higher rank. Image data to convert. Last dimension must be
      size 3.

  Returns:
    images: tensor with the same shape as `images`.
  """
images = ops.convert_to_tensor(images, name='images')
kernel = ops.convert_to_tensor(
    _rgb_to_yiq_kernel, dtype=images.dtype, name='kernel')
ndims = images.get_shape().ndims
exit(math_ops.tensordot(images, kernel, axes=[[ndims - 1], [0]]))
