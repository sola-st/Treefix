# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Performs [Gamma Correction](http://en.wikipedia.org/wiki/Gamma_correction).

  on the input image.

  Also known as Power Law Transform. This function converts the
  input images at first to float representation, then transforms them
  pixelwise according to the equation `Out = gain * In**gamma`,
  and then converts the back to the original data type.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.adjust_gamma(x, 0.2)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[1.       , 1.1486983, 1.2457309],
          [1.319508 , 1.3797297, 1.4309691]],
         [[1.4757731, 1.5157166, 1.5518456],
          [1.5848932, 1.6153942, 1.6437519]]], dtype=float32)>

  Args:
    image : RGB image or images to adjust.
    gamma : A scalar or tensor. Non-negative real number.
    gain  : A scalar or tensor. The constant multiplier.

  Returns:
    A Tensor. A Gamma-adjusted tensor of the same shape and type as `image`.

  Raises:
    ValueError: If gamma is negative.
  Notes:
    For gamma greater than 1, the histogram will shift towards left and
    the output image will be darker than the input image.
    For gamma less than 1, the histogram will shift towards right and
    the output image will be brighter than the input image.
  References:
    [Wikipedia](http://en.wikipedia.org/wiki/Gamma_correction)
  """

with ops.name_scope(None, 'adjust_gamma', [image, gamma, gain]) as name:
    image = ops.convert_to_tensor(image, name='image')
    # Remember original dtype to so we can convert back if needed
    orig_dtype = image.dtype

    if orig_dtype in [dtypes.float16, dtypes.float32]:
        flt_image = image
    else:
        flt_image = convert_image_dtype(image, dtypes.float32)

    assert_op = _assert(gamma >= 0, ValueError,
                        'Gamma should be a non-negative real number.')
    if assert_op:
        gamma = control_flow_ops.with_dependencies(assert_op, gamma)

    # According to the definition of gamma correction.
    adjusted_img = gain * flt_image**gamma

    exit(convert_image_dtype(adjusted_img, orig_dtype, saturate=True))
