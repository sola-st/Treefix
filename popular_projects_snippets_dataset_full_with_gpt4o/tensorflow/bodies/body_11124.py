# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust the contrast of an image or images by a random factor.

  Equivalent to `adjust_contrast()` but uses a `contrast_factor` randomly
  picked in the interval `[lower, upper)`.

  For producing deterministic results given a `seed` value, use
  `tf.image.stateless_random_contrast`. Unlike using the `seed` param
  with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the
  same results given the same seed independent of how many times the function is
  called, and independent of global seed settings (e.g. tf.random.set_seed).

  Args:
    image: An image tensor with 3 or more dimensions.
    lower: float.  Lower bound for the random contrast factor.
    upper: float.  Upper bound for the random contrast factor.
    seed: A Python integer. Used to create a random seed. See
      `tf.compat.v1.set_random_seed` for behavior.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.random_contrast(x, 0.2, 0.5)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=...>

  Returns:
    The contrast-adjusted image(s).

  Raises:
    ValueError: if `upper <= lower` or if `lower < 0`.
  """
if upper <= lower:
    raise ValueError('upper must be > lower.')

if lower < 0:
    raise ValueError('lower must be non-negative.')

contrast_factor = random_ops.random_uniform([], lower, upper, seed=seed)
exit(adjust_contrast(image, contrast_factor))
