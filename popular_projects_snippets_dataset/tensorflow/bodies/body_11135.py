# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Randomly changes jpeg encoding quality for inducing jpeg noise.

  `min_jpeg_quality` must be in the interval `[0, 100]` and less than
  `max_jpeg_quality`.
  `max_jpeg_quality` must be in the interval `[0, 100]`.

  Usage Example:

  >>> x = tf.constant([[[1, 2, 3],
  ...                   [4, 5, 6]],
  ...                  [[7, 8, 9],
  ...                   [10, 11, 12]]], dtype=tf.uint8)
  >>> tf.image.random_jpeg_quality(x, 75, 95)
  <tf.Tensor: shape=(2, 2, 3), dtype=uint8, numpy=...>

  For producing deterministic results given a `seed` value, use
  `tf.image.stateless_random_jpeg_quality`. Unlike using the `seed` param
  with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the
  same results given the same seed independent of how many times the function is
  called, and independent of global seed settings (e.g. tf.random.set_seed).

  Args:
    image: 3D image. Size of the last dimension must be 1 or 3.
    min_jpeg_quality: Minimum jpeg encoding quality to use.
    max_jpeg_quality: Maximum jpeg encoding quality to use.
    seed: An operation-specific seed. It will be used in conjunction with the
      graph-level seed to determine the real seeds that will be used in this
      operation. Please see the documentation of set_random_seed for its
      interaction with the graph-level random seed.

  Returns:
    Adjusted image(s), same shape and DType as `image`.

  Raises:
    ValueError: if `min_jpeg_quality` or `max_jpeg_quality` is invalid.
  """
if (min_jpeg_quality < 0 or max_jpeg_quality < 0 or min_jpeg_quality > 100 or
    max_jpeg_quality > 100):
    raise ValueError('jpeg encoding range must be between 0 and 100.')

if min_jpeg_quality >= max_jpeg_quality:
    raise ValueError('`min_jpeg_quality` must be less than `max_jpeg_quality`.')

jpeg_quality = random_ops.random_uniform([],
                                         min_jpeg_quality,
                                         max_jpeg_quality,
                                         seed=seed,
                                         dtype=dtypes.int32)
exit(adjust_jpeg_quality(image, jpeg_quality))
