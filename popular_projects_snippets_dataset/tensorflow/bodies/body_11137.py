# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust jpeg encoding quality of an image.

  This is a convenience method that converts an image to uint8 representation,
  encodes it to jpeg with `jpeg_quality`, decodes it, and then converts back
  to the original data type.

  `jpeg_quality` must be in the interval `[0, 100]`.

  Usage Examples:

  >>> x = [[[0.01, 0.02, 0.03],
  ...       [0.04, 0.05, 0.06]],
  ...      [[0.07, 0.08, 0.09],
  ...       [0.10, 0.11, 0.12]]]
  >>> x_jpeg = tf.image.adjust_jpeg_quality(x, 75)
  >>> x_jpeg.numpy()
  array([[[0.00392157, 0.01960784, 0.03137255],
          [0.02745098, 0.04313726, 0.05490196]],
         [[0.05882353, 0.07450981, 0.08627451],
          [0.08235294, 0.09803922, 0.10980393]]], dtype=float32)

  Note that floating point values are expected to have values in the range
  [0,1) and values outside this range are clipped.

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.adjust_jpeg_quality(x, 75)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[1., 1., 1.],
          [1., 1., 1.]],
         [[1., 1., 1.],
          [1., 1., 1.]]], dtype=float32)>

  Note that `jpeg_quality` 100 is still lossy compresson.

  >>> x = tf.constant([[[1, 2, 3],
  ...                   [4, 5, 6]],
  ...                  [[7, 8, 9],
  ...                   [10, 11, 12]]], dtype=tf.uint8)
  >>> tf.image.adjust_jpeg_quality(x, 100)
  <tf.Tensor: shape(2, 2, 3), dtype=uint8, numpy=
  array([[[ 0,  1,  3],
          [ 3,  4,  6]],
         [[ 6,  7,  9],
          [ 9, 10, 12]]], dtype=uint8)>

  Args:
    image: 3D image. The size of the last dimension must be None, 1 or 3.
    jpeg_quality: Python int or Tensor of type int32. jpeg encoding quality.
    name: A name for this operation (optional).

  Returns:
    Adjusted image, same shape and DType as `image`.

  Raises:
    InvalidArgumentError: quality must be in [0,100]
    InvalidArgumentError: image must have 1 or 3 channels
  """
with ops.name_scope(name, 'adjust_jpeg_quality', [image]):
    image = ops.convert_to_tensor(image, name='image')
    channels = image.shape.as_list()[-1]
    # Remember original dtype to so we can convert back if needed
    orig_dtype = image.dtype
    image = convert_image_dtype(image, dtypes.uint8, saturate=True)
    if not _is_tensor(jpeg_quality):
        # If jpeg_quality is a int (not tensor).
        jpeg_quality = ops.convert_to_tensor(jpeg_quality, dtype=dtypes.int32)
    image = gen_image_ops.encode_jpeg_variable_quality(image, jpeg_quality)

    image = gen_image_ops.decode_jpeg(image, channels=channels)
    exit(convert_image_dtype(image, orig_dtype, saturate=True))
