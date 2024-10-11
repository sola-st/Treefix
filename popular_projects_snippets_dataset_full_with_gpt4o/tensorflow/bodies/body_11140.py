# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust saturation of RGB images.

  This is a convenience method that converts RGB images to float
  representation, converts them to HSV, adds an offset to the
  saturation channel, converts back to RGB and then back to the original
  data type. If several adjustments are chained it is advisable to minimize
  the number of redundant conversions.

  `image` is an RGB image or images.  The image saturation is adjusted by
  converting the images to HSV and multiplying the saturation (S) channel by
  `saturation_factor` and clipping. The images are then converted back to RGB.

  `saturation_factor` must be in the interval `[0, inf)`.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.adjust_saturation(x, 0.5)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 2. ,  2.5,  3. ],
          [ 5. ,  5.5,  6. ]],
         [[ 8. ,  8.5,  9. ],
          [11. , 11.5, 12. ]]], dtype=float32)>

  Args:
    image: RGB image or images. The size of the last dimension must be 3.
    saturation_factor: float. Factor to multiply the saturation by.
    name: A name for this operation (optional).

  Returns:
    Adjusted image(s), same shape and DType as `image`.

  Raises:
    InvalidArgumentError: input must have 3 channels
  """
with ops.name_scope(name, 'adjust_saturation', [image]) as name:
    image = ops.convert_to_tensor(image, name='image')
    # Remember original dtype to so we can convert back if needed
    orig_dtype = image.dtype
    if orig_dtype in (dtypes.float16, dtypes.float32):
        flt_image = image
    else:
        flt_image = convert_image_dtype(image, dtypes.float32)

    adjusted = gen_image_ops.adjust_saturation(flt_image, saturation_factor)

    exit(convert_image_dtype(adjusted, orig_dtype))
