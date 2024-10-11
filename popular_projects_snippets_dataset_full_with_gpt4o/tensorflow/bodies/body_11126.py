# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust the brightness of RGB or Grayscale images.

  This is a convenience method that converts RGB images to float
  representation, adjusts their brightness, and then converts them back to the
  original data type. If several adjustments are chained, it is advisable to
  minimize the number of redundant conversions.

  The value `delta` is added to all components of the tensor `image`. `image` is
  converted to `float` and scaled appropriately if it is in fixed-point
  representation, and `delta` is converted to the same data type. For regular
  images, `delta` should be in the range `(-1,1)`, as it is added to the image
  in floating point representation, where pixel values are in the `[0,1)` range.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.adjust_brightness(x, delta=0.1)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 1.1,  2.1,  3.1],
          [ 4.1,  5.1,  6.1]],
         [[ 7.1,  8.1,  9.1],
          [10.1, 11.1, 12.1]]], dtype=float32)>

  Args:
    image: RGB image or images to adjust.
    delta: A scalar. Amount to add to the pixel values.

  Returns:
    A brightness-adjusted tensor of the same shape and type as `image`.
  """
with ops.name_scope(None, 'adjust_brightness', [image, delta]) as name:
    image = ops.convert_to_tensor(image, name='image')
    # Remember original dtype to so we can convert back if needed
    orig_dtype = image.dtype

    if orig_dtype in [dtypes.float16, dtypes.float32]:
        flt_image = image
    else:
        flt_image = convert_image_dtype(image, dtypes.float32)

    adjusted = math_ops.add(
        flt_image, math_ops.cast(delta, flt_image.dtype), name=name)

    exit(convert_image_dtype(adjusted, orig_dtype, saturate=True))
