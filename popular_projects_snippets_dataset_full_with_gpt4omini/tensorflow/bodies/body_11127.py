# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust contrast of RGB or grayscale images.

  This is a convenience method that converts RGB images to float
  representation, adjusts their contrast, and then converts them back to the
  original data type. If several adjustments are chained, it is advisable to
  minimize the number of redundant conversions.

  `images` is a tensor of at least 3 dimensions.  The last 3 dimensions are
  interpreted as `[height, width, channels]`.  The other dimensions only
  represent a collection of images, such as `[batch, height, width, channels].`

  Contrast is adjusted independently for each channel of each image.

  For each channel, this Op computes the mean of the image pixels in the
  channel and then adjusts each component `x` of each pixel to
  `(x - mean) * contrast_factor + mean`.

  `contrast_factor` must be in the interval `(-inf, inf)`.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.adjust_contrast(x, 2.)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[-3.5, -2.5, -1.5],
          [ 2.5,  3.5,  4.5]],
         [[ 8.5,  9.5, 10.5],
          [14.5, 15.5, 16.5]]], dtype=float32)>

  Args:
    images: Images to adjust.  At least 3-D.
    contrast_factor: A float multiplier for adjusting contrast.

  Returns:
    The contrast-adjusted image or images.
  """
with ops.name_scope(None, 'adjust_contrast',
                    [images, contrast_factor]) as name:
    images = ops.convert_to_tensor(images, name='images')
    # Remember original dtype to so we can convert back if needed
    orig_dtype = images.dtype

    if orig_dtype in (dtypes.float16, dtypes.float32):
        flt_images = images
    else:
        flt_images = convert_image_dtype(images, dtypes.float32)

    adjusted = gen_image_ops.adjust_contrastv2(
        flt_images, contrast_factor=contrast_factor, name=name)

    exit(convert_image_dtype(adjusted, orig_dtype, saturate=True))
