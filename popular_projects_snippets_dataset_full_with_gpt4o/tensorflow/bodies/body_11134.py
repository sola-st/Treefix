# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust hue of RGB images.

  This is a convenience method that converts an RGB image to float
  representation, converts it to HSV, adds an offset to the
  hue channel, converts back to RGB and then back to the original
  data type. If several adjustments are chained it is advisable to minimize
  the number of redundant conversions.

  `image` is an RGB image.  The image hue is adjusted by converting the
  image(s) to HSV and rotating the hue channel (H) by
  `delta`.  The image is then converted back to RGB.

  `delta` must be in the interval `[-1, 1]`.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.adjust_hue(x, 0.2)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 2.3999996,  1.       ,  3.       ],
          [ 5.3999996,  4.       ,  6.       ]],
        [[ 8.4      ,  7.       ,  9.       ],
          [11.4      , 10.       , 12.       ]]], dtype=float32)>

  Args:
    image: RGB image or images. The size of the last dimension must be 3.
    delta: float.  How much to add to the hue channel.
    name: A name for this operation (optional).

  Returns:
    Adjusted image(s), same shape and DType as `image`.

  Raises:
    InvalidArgumentError: image must have at least 3 dimensions.
    InvalidArgumentError: The size of the last dimension must be 3.
    ValueError: if `delta` is not in the interval of `[-1, 1]`.

  Usage Example:

  >>> image = [[[1, 2, 3], [4, 5, 6]],
  ...          [[7, 8, 9], [10, 11, 12]],
  ...          [[13, 14, 15], [16, 17, 18]]]
  >>> image = tf.constant(image)
  >>> tf.image.adjust_hue(image, 0.2)
  <tf.Tensor: shape=(3, 2, 3), dtype=int32, numpy=
  array([[[ 2,  1,  3],
        [ 5,  4,  6]],
       [[ 8,  7,  9],
        [11, 10, 12]],
       [[14, 13, 15],
        [17, 16, 18]]], dtype=int32)>
  """
with ops.name_scope(name, 'adjust_hue', [image]) as name:
    if context.executing_eagerly():
        if delta < -1 or delta > 1:
            raise ValueError('delta must be in the interval [-1, 1]')
    image = ops.convert_to_tensor(image, name='image')
    # Remember original dtype to so we can convert back if needed
    orig_dtype = image.dtype
    if orig_dtype in (dtypes.float16, dtypes.float32):
        flt_image = image
    else:
        flt_image = convert_image_dtype(image, dtypes.float32)

    rgb_altered = gen_image_ops.adjust_hue(flt_image, delta)

    exit(convert_image_dtype(rgb_altered, orig_dtype))
