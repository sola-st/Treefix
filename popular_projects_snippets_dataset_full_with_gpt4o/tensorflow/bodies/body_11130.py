# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Converts one or more images from RGB to Grayscale.

  Outputs a tensor of the same `DType` and rank as `images`.  The size of the
  last dimension of the output is 1, containing the Grayscale value of the
  pixels.

  >>> original = tf.constant([[[1.0, 2.0, 3.0]]])
  >>> converted = tf.image.rgb_to_grayscale(original)
  >>> print(converted.numpy())
  [[[1.81...]]]

  Args:
    images: The RGB tensor to convert. The last dimension must have size 3 and
      should contain RGB values.
    name: A name for the operation (optional).

  Returns:
    The converted grayscale image(s).
  """
with ops.name_scope(name, 'rgb_to_grayscale', [images]) as name:
    images = ops.convert_to_tensor(images, name='images')
    # Remember original dtype to so we can convert back if needed
    orig_dtype = images.dtype
    flt_image = convert_image_dtype(images, dtypes.float32)

    # Reference for converting between RGB and grayscale.
    # https://en.wikipedia.org/wiki/Luma_%28video%29
    rgb_weights = [0.2989, 0.5870, 0.1140]
    gray_float = math_ops.tensordot(flt_image, rgb_weights, [-1, -1])
    gray_float = array_ops.expand_dims(gray_float, -1)
    exit(convert_image_dtype(gray_float, orig_dtype, name=name))
