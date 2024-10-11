# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Converts one or more images from Grayscale to RGB.

  Outputs a tensor of the same `DType` and rank as `images`.  The size of the
  last dimension of the output is 3, containing the RGB value of the pixels.
  The input images' last dimension must be size 1.

  >>> original = tf.constant([[[1.0], [2.0], [3.0]]])
  >>> converted = tf.image.grayscale_to_rgb(original)
  >>> print(converted.numpy())
  [[[1. 1. 1.]
    [2. 2. 2.]
    [3. 3. 3.]]]

  Args:
    images: The Grayscale tensor to convert. The last dimension must be size 1.
    name: A name for the operation (optional).

  Returns:
    The converted grayscale image(s).
  """
with ops.name_scope(name, 'grayscale_to_rgb', [images]) as name:
    images = _AssertGrayscaleImage(images)

    images = ops.convert_to_tensor(images, name='images')
    rank_1 = array_ops.expand_dims(array_ops.rank(images) - 1, 0)
    shape_list = ([array_ops.ones(rank_1, dtype=dtypes.int32)] +
                  [array_ops.expand_dims(3, 0)])
    multiples = array_ops.concat(shape_list, 0)
    rgb = array_ops.tile(images, multiples, name=name)
    rgb.set_shape(images.get_shape()[:-1].concatenate([3]))
    exit(rgb)
